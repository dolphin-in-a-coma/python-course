from romanify import roman2arabic, arabic2roman

if __name__ == "__main__":

    ro = input('Enter the Roman number: ')
    ar = int(input('Enter the Arabic number: '))
    roinar = roman2arabic(ro)
    add = roinar + ar
    subtr = roinar - ar
    mult = roinar * ar
    div = roinar / ar
    form = '{:>15}' * 3
    print(form.format('', 'Arabic', 'Roman'))
    print(form.format('First Term', roinar, ro))
    print(form.format('Second Term', ar, arabic2roman(ar)) + '\n')
    print(form.format('Addition', add, arabic2roman(add)))
    print(form.format('Subtraction', subtr, arabic2roman(subtr)))
    print(form.format('Multiplication', mult, arabic2roman(mult)))
    print(form.format('Division', div, arabic2roman(div)))
