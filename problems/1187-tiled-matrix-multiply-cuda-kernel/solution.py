#include <cuda_runtime.h>

__global__ void matmul_kernel(const float* A, const float* B, float* C, int M, int N, int K) {
    int j = blockIdx.x * blockDim.x + threadIdx.x;
    int i = blockIdx.y * blockDim.y + threadIdx.y;

    if (i < M && j < N) {
        float sum = 0.0f;

        for (int k = 0; k < K; k++) {
            sum += A[i * K + k] * B[k * N + j];
        }

        C[i * N + j] = sum;
    }
}

void solve(const float* A, const float* B, float* C, int M, int N, int K) {
    // TODO: allocate device memory, copy in, launch kernel, copy out, free
    float *d_A, *d_B, *d_C;
    dim3 grid((N + 31) / 32, (M + 31) / 32), block(32, 32);
    
    cudaMalloc(&d_A, M * K * sizeof(float));
    cudaMalloc(&d_B, K * N * sizeof(float));
    cudaMalloc(&d_C, M * N * sizeof(float));

    cudaMemcpy(
        d_A,
        A,
        M * K * sizeof(float),
        cudaMemcpyHostToDevice
    );
    cudaMemcpy(
        d_B,
        B,
        K * N * sizeof(float),
        cudaMemcpyHostToDevice
    );

    matmul_kernel<<<grid, block>>>(d_A, d_B, d_C, M, N, K);

    cudaMemcpy(
        C, 
        d_C, 
        M * N * sizeof(float), 
        cudaMemcpyDeviceToHost
    );

    cudaFree(d_A);
    cudaFree(d_B);
    cudaFree(d_C);

    return;
}