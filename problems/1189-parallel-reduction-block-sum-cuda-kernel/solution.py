#include <cuda_runtime.h>

#define THREADS_PER_BLOCK 1024

__global__ void kernel(const float* in, float* out, int N) {
    // TODO: block-wise reduction using shared memory
    __shared__ float sdata[THREADS_PER_BLOCK];

    int local_idx = threadIdx.x;
    int global_idx = blockIdx.x * blockDim.x + local_idx;

    if (global_idx < N) {
        sdata[local_idx] = in[global_idx]; 
    } else {
        sdata[local_idx] = 0.0f;
    }

    __syncthreads();

    for (int stride = blockDim.x / 2; stride > 0; stride /= 2) {
        if (local_idx < stride) {
            sdata[local_idx] += sdata[local_idx + stride];
        }

        __syncthreads();
    }

    if (local_idx == 0) {
        atomicAdd(out, sdata[0]);
    }
}

void solve(const float* input, float* output, int N) {
    // TODO: allocate device memory, copy in, launch kernel, copy out, free
    float *d_input, *d_output;

    cudaMalloc(&d_input, N * sizeof(float));
    cudaMalloc(&d_output, sizeof(float));

    cudaMemcpy(
        d_input,
        input,
        N * sizeof(float),
        cudaMemcpyHostToDevice
    );

    cudaMemset(d_output, 0, sizeof(float));

    kernel<<<(N + THREADS_PER_BLOCK - 1) / THREADS_PER_BLOCK, THREADS_PER_BLOCK>>>(d_input, d_output, N);

    cudaMemcpy(
        output,
        d_output,
        sizeof(float),
        cudaMemcpyDeviceToHost
    );

    cudaFree(d_input);
    cudaFree(d_output);

    return;
}