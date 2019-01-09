from election_analyzer import ElectionAnalyzer

if __name__ == "__main__":

    ea = ElectionAnalyzer()
    try:
        ea.load(filename="data_2016-09-18.csv")

        print(ea)

        ea.show_plot()
    except Exception as err:
        print("Во время работы приложения произошла ошибка:", err)
        raise
