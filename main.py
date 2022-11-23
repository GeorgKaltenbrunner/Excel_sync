import glob
import pandas as pd


def get_excel_data(seperator, regre_method):
    # DataFrame to store all the Data from the Excel Files
    validation_df = pd.DataFrame()

    for file in glob.glob('*.xlsx'):
        filename = file

        # Read Excelfile
        df = pd.read_excel(filename)

        # Get data from Excel -> Here specify the columns needed
        early_orders = df.loc[df['Replication_Nr'] == 'Mean']['Early Ratio'].item()
        tardy_orders = df.loc[df['Replication_Nr'] == 'Mean']['Tardy Ratio'].item()
        earliness = df.loc[df['Replication_Nr'] == 'Mean']['Earliness'].item()
        tardiness = df.loc[df['Replication_Nr'] == 'Mean']['Tardiness'].item()
        avg_sftt = df.loc[df['Replication_Nr'] == 'Mean']['Avg_SFTT'].item()
        prognose_mean = df['Prognosegüte'].mean()

        # Extract name for column
        file_split = filename.split(".xlsx")
        file_split_name_column = file_split[0].split(seperator)
        file_column = file_split_name_column[0] + regre_method + file_split_name_column[1]
        print(file_split_name_column)

        # New Dataframe -> to store the needed information
        df_file = pd.DataFrame({'Early_Orders_Ratio': early_orders,
                                'Tardy_Orders_Ratio': tardy_orders,
                                'Earliness': earliness,
                                'Tardiness': tardiness,
                                'Avg_SFTT': avg_sftt,
                                'Prognosegüte': prognose_mean}, index=[file_column])

        validation_df = pd.concat([validation_df, df_file])

        print()


if __name__ == "__main__":
    get_excel_data("_EXP_ALL_DEMAND_", "_EXP_ALL_DEMAND_")
