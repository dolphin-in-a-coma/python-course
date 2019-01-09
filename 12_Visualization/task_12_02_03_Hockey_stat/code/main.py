from iihf_analyzer import IihfAnalyzer

if __name__ == "__main__":

    analyzer = IihfAnalyzer()
    try:
        analyzer.load(filename="hockey_players.csv")
        '''print(analyzer.countries)
        print(analyzer.years)
        print(analyzer.fields)
        print(analyzer._data)'''
        #print(analyzer)
        #print(analyzer._get_players_without_dublicates(analyzer._data))

        analyzer.show_plot()
    except Exception as err:
        print("Во время работы приложения произошла ошибка:", err)
        raise
