import numpy as np

# Task 1: Creating Arrays

array_1d = np.arange(1, 11)
array_2d = np.arange(1, 10).reshape(3, 3)
array_3d = np.random.rand(3, 5, 3)

print("TASK 1 :\n")
print("1D Array:",array_1d)
print("Shape:", array_1d.shape)
print("Size:", array_1d.size)
print("Datatype:", array_1d.dtype,"\n")

print("2D Array:",array_2d)
print("Shape:", array_2d.shape)
print("Size:", array_2d.size)
print("Datatype:", array_2d.dtype,"\n")

print("3D Array:",array_3d)
print("Shape:", array_3d.shape)
print("Size:", array_3d.size)
print("Datatype:", array_3d.dtype)
print("\n\n")


# Task 2: Array Indexing and Slicing

data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
numpy_array = np.array(data)

first_three = numpy_array[:3]
alternate_elements = numpy_array[::2]
reversed_array = numpy_array[::-1]

print("TASK 2 :\n")
print("First three elements:", first_three)
print("Alternate elements:", alternate_elements)
print("Reversed array:", reversed_array)
print("\n\n")


# Task 3: Mathematical Operations

arr_A = np.random.randint(1, 21, 5)
arr_B = np.random.randint(1, 21, 5)

arr_add = arr_A + arr_B
arr_sub = arr_A - arr_B
arr_mul = arr_A * arr_B
arr_div = arr_A / arr_B

dot_product = np.dot(arr_A, arr_B)

mean_A = np.mean(arr_A)
median_A = np.median(arr_A)
std_dev_A = np.std(arr_A)
variance_A = np.var(arr_A)

max_B = np.max(arr_B)
min_B = np.min(arr_B)
max_index_B = np.argmax(arr_B)
min_index_B = np.argmin(arr_B)

print("TASK 3 :\n")
print("Array A:", arr_A)
print("Array B:", arr_B)
print("Addition:", arr_add)
print("Subtraction:", arr_sub)
print("Multiplication:", arr_mul)
print("Division:", arr_div)
print("Dot Product:", dot_product)
print("Mean of A:", mean_A)
print("Median of A:", median_A)
print("Standard Deviation of A:", std_dev_A)
print("Variance of A:", variance_A)
print("Maximum of B:", max_B, "at index", max_index_B)
print("Minimum of B:", min_B, "at index", min_index_B)
print("\n\n")


# Task 4: Reshaping and Transposing

array_1d_12 = np.arange(1, 13)
reshaped_2d = array_1d_12.reshape(4, 3)
reshaped_3d = array_1d_12.reshape(2, 2, 3)
transposed_2d = reshaped_2d.T
transposed_shape = transposed_2d.shape

print("TASK 4 :\n")
print("Original 1D Array (1-12): ", array_1d_12)
print("Reshaped 2D Array (4,3): ", reshaped_2d)
print("Reshaped 3D Array (2,2,3): ", reshaped_3d)
print("Transposed 2D Array: ", transposed_2d)
print("Shape of Transposed 2D Array: ", transposed_shape)
print("\n\n")


# Task 5: Boolean Masking and Filtering

random_array = np.random.randint(10, 51, 15)
greater_than_25 = random_array[random_array > 25]
modified_array = np.copy(random_array)
modified_array[modified_array < 30] = 0
div_by_5 = np.sum(random_array % 5 == 0)

print("TASK 5 :\n")
print("Original Random Array:", random_array)
print("Elements greater than 25:", greater_than_25)
print("Array with elements less than 30 replaced by 0:", modified_array)
print("Number of elements divisible by 5:", div_by_5)
print("\n\n")


# Task 6: Working with Built-in Functions

linspace_array = np.linspace(0, 1, 10)
identity_matrix = np.eye(4)
random_integers = np.random.randint(1, 101, 20)
sorted_integers = np.sort(random_integers)
largest_5 = sorted_integers[-5:]

print("TASK 6 :\n")
print("10 equally spaced values between 0 and 1:", linspace_array)
print("4x4 Identity Matrix:", identity_matrix)
print("Original 20 random integers (1-100):", random_integers)
print("Sorted integers:", sorted_integers)
print("5 largest elements:", largest_5)
print("\n\n")


# Task 7: Generic

import time

matrix_A = np.random.rand(100, 100)
matrix_B = np.random.rand(100, 100)

start_time = time.time()

matrix_C = np.dot(matrix_A, matrix_B)
determinant_C = np.linalg.det(matrix_C)
inverse_C = np.linalg.inv(matrix_C)
det_inv_C = f"Determinant of C: {determinant_C:.4f}\nInverse of C:\n{inverse_C}"

end_time = time.time()
time_taken = end_time - start_time

print("TASK 7 :\n")
print("Matrix A :", matrix_A[:3, :3])
print("Matrix B :", matrix_B[:3, :3])
print("Resulting Matrix C :", matrix_C[:3, :3])
print(det_inv_C,"\n")
print(f"Time taken for operations: {time_taken:.4f} seconds")