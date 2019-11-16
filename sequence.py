# This file contains a class declaration.
# I have included the initializer and an example method to help you.
# You will need to add the other methods yourself.
import matplotlib.pyplot as plt

class Sequence:

    # This method is the initializer, it is called when creating (instantiating) an object (instance) of this class.
    def __init__(self, bases):
        # store the bases as an attribute.
        self.bases = bases

    # This is an example method, it returns the first base.
    def first_base(self):
        # We can access the 'bases' for this instance via 'self'.
        result = self.bases[0]
        return result

    # TODO: add other methods here to complete the tasks.

    # Task 2.
    # The number of DNA bases (i.e. characters) in the sequence.
    def number_dna_bases(self):
        sum=0
        for num in self.bases:
            sum+=1
        return sum

    # Task 3.
    # validates whether the all the characters are valid
    # DNA bases: A,T, C or G. It should return True or False. If the sequence has zero length, it should return
    # False.
    def  is_dna(self):

      if len(self.bases)== 0:
        flag = False
        #break
      for char in self.bases:
         flag = False
         #print(char)
         if (char == ( 'A') or char == ( 'T')  or char == ('C') or char == ( 'G')):
           flag = True
         else:
           flag = False
           break

      return flag

    # Task 4.
    # returns the complement of the Sequence as a new Sequence instance.
    def complement(self):

        new = list(self.bases) #convert str to list
        temp_new = list(self.bases)

        new[0] = temp_new[3]
        new[3] = temp_new[0]
        new[1] = temp_new[2]
        new[2] = temp_new[1]

        new_str = ''.join(new) #convert list to str

        return new_str

    #Task 5.
    #finds the first pair of non-matching bases, when comparing with
    #another Sequence instance.
    def nonmatching_bases(self):

        another_Sequence ='AGTT'

        if len(self.bases) == 0 or len(another_Sequence) == 0:
           Num = -1
           return Num

        new = list(self.bases)  # convert str to list
        another_new = list(another_Sequence)

        if new == another_new:
            Num = -1

        if new[0] != another_new[0]:
            Num = 0

        if new[1] != another_new[1]:
            Num = 1

        if new[2] != another_new[2]:
            Num = 2

        if new[3] != another_new[3]:
            Num = 3

        return Num

    # Task 7.
    # Create a method (on the class) which splits the sequence into genes.
    def splits(self):

        x = self.bases.find("AAAAAAAAAATTTTTTTTTT")
        print("A new Sequence(gene):",self.bases[0:x])
        print("The length of the first gene:", x )


    # Task 8.
    # Use your method to create a list of Sequence instances from genome_01.dat, each containing a
    #single gene. Plot the gene lengths as a histogram using matplotlib.
    # Save the plot as a PNG image, ensure it has a title and axis labels.
    def list_of_Sequence(self):
        N =[]
        with open('genome_01.dat') as f:
            lines = f.readlines()
            for line in lines[1:]:
                words = line.split('AAAAAAAAAATTTTTTTTTT')
                #print(words)
            for num in words[0:]:
                N.append(len(num))
            print("N",N)

        x = []
        y = []

        plt.plot(N , label = 'The gene lengths')
        plt.xlabel('x')
        plt.title(' A single genes ')
        plt.legend()
        plt.show()
        plt.savefig('fig.png')

    # Task 9.
    # Write a method (on the class) which compares the DNA sequence with another, and returns the
    # number of "swap" mutations – bases which do not match.

    def  Swap(self):

      with open('genome_01.dat') as f1:
         lines1 = f1.readlines()
         for line1 in lines1[1:]:
            words1 = line1.split('AAAAAAAAAATTTTTTTTTT')
            #print("words1", words1 )

      with open('genome_02.dat') as f2:
         lines2 = f2.readlines()
         for line2 in lines2[1:]:
             words2 = line2.split('AAAAAAAAAATTTTTTTTTT')
             #print("words2", words2)

      i = 0
      l = []
      while  i < len(words1):
             s = 0
             if words1[i] != words2[i]:

                list_gen1 = list(words1[i])  # convert str to list
                list_gen2 = list(words2[i])

                m = 0
                for k in list_gen1:
                  if k != list_gen2[m]:
                        s+=1
                  m+=1

             l.append(s)
             #print(s)
             i+=1

      return l


