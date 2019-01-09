import vector
import random

if __name__ == "__main__":

    try:
        list1 = random.sample(range(-10, 20), 4)
        list2 = random.sample(range(-10, 20), 4)
        text = '\n\t First: {}\n\tSecond: {}\n'
        print('Values:' + text.format(list1, list2))
        vect1 = vector.create(*list1)
        vect2 = vector.create(*list2)
        print('Vectors:' + text.format(vect1, vect2))
        print('is_vector:\n')
        print('   Values:' + text.format(vector.is_vector(list1),
                                         vector.is_vector(list2)))
        print('   Vectors:' + text.format(vector.is_vector(vect1),
                                          vector.is_vector(vect2)))
        print('Length:' + text.format(vector.length(vect1),
              vector.length(vect2)))
        a = random.randrange(-15, 30)
        b = round(random.uniform(-15, 30), 4)
        print('Multiplication:' +
              '\n\tFirst and {}: {}\n\tSecond  and {}: {}\n'
              .format(a, vector.multiply(vect1, a), b,
                      vector.multiply(vect2, b)))
        print('Scalar multiplication:',
              round(vector.scalar_product(vect1, vect2), 4))
        print('\nAngle:', vector.angle_between(vect1, vect2))

    except Exception as err:
        print('Error occured during execution:', err)
        print('Type:', type(err))

