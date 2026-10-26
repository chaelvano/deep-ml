#include <cuda_runtime.h>
#include <vector>

__global__ void index_kernel(int* out, int n) {
    // Compute this thread's global index and, if it is < n, write it to out.
    int i = blockIdx.x * blockDim.x + threadIdx.x;

    if (i < n) {
        out[i] = i;
    }
}

std::vector<int> global_thread_indices(int n) {
    // 1. allocate device memory for n ints
    std::vector<int> h_data(n);
    int* d_data;
    
    cudaMalloc(&d_data, n * sizeof(int));

    // 2. launch the kernel with enough threads to cover n
    index_kernel<<<(n + 1023) / 1024, 1024>>>(d_data, n);

    // 3. copy the result back to the host and return it
    cudaMemcpy(
        h_data.data(),
        d_data,
        n * sizeof(int),
        cudaMemcpyDeviceToHost
    );

    cudaFree(d_data);

    return h_data;
}
