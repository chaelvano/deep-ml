#include <cuda_runtime.h>
#include <vector>

__global__ void add_kernel(const float* a, const float* b, float* c, int n) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;

    if (i < n) {
        c[i] = a[i] + b[i];
    }
}

std::vector<float> vector_add(const std::vector<float>& a, const std::vector<float>& b) {
    // allocate a, b, c on the device; copy a and b over (Host -> Device);
    int n = a.size();

    std::vector<float> c(n);
    float *d_a, *d_b, *d_c;

    cudaMalloc(&d_a, n * sizeof(float));
    cudaMalloc(&d_b, n * sizeof(float));
    cudaMalloc(&d_c, n * sizeof(float));

    cudaMemcpy(
        d_a,
        a.data(),
        n * sizeof(float),
        cudaMemcpyHostToDevice
    );
    cudaMemcpy(
        d_b,
        b.data(),
        n * sizeof(float),
        cudaMemcpyHostToDevice
    );

    // launch the kernel; copy c back; free memory
    add_kernel<<<(n + 1023) / 1024, 1024>>>(d_a, d_b, d_c, n);

    cudaMemcpy(
        c.data(),
        d_c,
        n * sizeof(float),
        cudaMemcpyDeviceToHost
    );

    cudaFree(d_a);
    cudaFree(d_b);
    cudaFree(d_c);

    return c;
}
