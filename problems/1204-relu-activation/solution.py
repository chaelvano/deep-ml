#include <cuda_runtime.h>
#include <vector>

__global__ void relu_kernel(const float* x, float* out, int n) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;

    if (i < n) {
        out[i] = fmaxf(0.0f, x[i]);
    }
}

std::vector<float> relu(const std::vector<float>& x) {
    int n = x.size();
    
    std::vector<float> y(n);
    float *d_x, *d_y;

    cudaMalloc(&d_x, n * sizeof(float));
    cudaMalloc(&d_y, n * sizeof(float));

    cudaMemcpy(
        d_x, 
        x.data(), 
        n * sizeof(float), 
        cudaMemcpyHostToDevice
    );

    relu_kernel<<<(n + 1023) / 1024, 1024>>>(d_x, d_y, n);

    cudaMemcpy(
        y.data(), 
        d_y, 
        n * sizeof(float), 
        cudaMemcpyDeviceToHost
    );

    cudaFree(d_x);
    cudaFree(d_y);

    return y;
}
