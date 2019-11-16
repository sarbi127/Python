import sequence
import matplotlib.pyplot as plt
import numpy as np




# Create an instance of the Sequence class.
example_sequence1 = sequence.Sequence('AGCT')

example2_sequence2 = sequence.Sequence('TTTCCGATCGARRAAAAAAAAAATTTTTTTTTT')


# Call the first_base method on our instance. Notice that we don't specify the 'self' parameter when we call the method.
example_first_base = example_sequence1.first_base()
print(f'The first base is: {example_first_base}')


# TODO add method calls to complete the tasks.

# Task 2.
example_number_dna_bases = example_sequence1.number_dna_bases()
print(f'The number of DNA bases is: {example_number_dna_bases}')

# Task 3.
example_is_dna = example_sequence1.is_dna()
print(f'The number of DNA bases is: {example_is_dna}')

# Task 4.
example_complement= example_sequence1.complement()
print(f'The complement of the Sequence is: {example_complement}')

# Task 5.
example_nonmatching_bases= example_sequence1.nonmatching_bases()
print(f'The complement of the Sequence is: {example_nonmatching_bases}')

# Task 6.
#Call the function to read the file "genome_01.dat", and print the total
#number of bases it contains by calling the method you implemented earlier.
def total_number_bases(file):
        characters = 0
        for line in file:
            wordslist = line.split()
            characters += sum(len(word) for word in wordslist)
        print("The total number of bases:", characters)

f = open("genome_01.dat", "r")
total_number_bases(f)

# Task 7.
example2_splits = example2_sequence2.splits()
#print(f'The complement of the Sequence is: {example2_splits}')

# Task 8.
example_list_of_Sequence= example_sequence1.list_of_Sequence()

# Task 9.
example_Swap= example_sequence1.Swap()
print( f'The number of "swap" mutations are: {example_Swap}')

N = [639, 1733, 1296, 915, 843, 1811, 1463, 1113, 1827, 357, 1858, 1908, 679, 1174, 1576, 680, 1500, 394, 785, 1590,
     631, 167, 254, 1704, 929, 1781, 617, 925, 152, 857, 195, 1056, 835, 1813, 1951, 1535, 528, 930, 179, 1281, 835,
     877, 739, 1251, 990, 503, 1392, 1369, 777, 719, 624, 623, 794, 324, 231, 755, 590, 1563, 962, 1287, 108, 882, 208,
     208, 1157, 1654, 1592, 836, 353, 415, 468, 1721, 1146, 1546, 623, 968, 337, 1425, 137, 371, 1974, 1223, 859, 510,
     1186, 171, 478, 691, 1669, 988, 713, 164, 283, 404, 854, 1044, 1151, 719, 1235, 5883]
l = [0, 12, 0, 4, 2, 1, 3, 2, 8, 0, 0, 0, 2, 6, 4, 1, 9, 3, 3, 5, 1, 0, 0, 5, 7, 9, 2, 6, 0, 4, 0, 5, 3, 8, 4, 10, 3, 7,
     0, 2, 2, 2, 0, 6, 6, 1, 4, 3, 1, 0, 4, 5, 2, 1, 0, 1, 3, 0, 0, 8, 0, 8, 0, 0, 0, 7, 9, 3, 1, 0, 0, 3, 4, 2, 2, 4,
     0, 1, 0, 0, 0, 5, 4, 4, 0, 0, 0, 2, 5, 2, 0, 0, 2, 2, 0, 3, 6, 1, 2, 0]

rng = np.random.RandomState(0)
colors = rng.rand(100)
sizes = 1000 * rng.rand(100)
#area = np.pi*3

# Plot
plt.scatter(N, l, c=colors, s=sizes, alpha=0.3, cmap='viridis')
plt.title('Scatter plot')
plt.xlabel('Gene length')
plt.ylabel('The number of swap mutations per gene')
plt.colorbar();  # show color scale
plt.show()