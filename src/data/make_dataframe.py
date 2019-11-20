def get_sheet(xls, num):
    """This function extracts the data from a worksheet and puts it in a DataFrame and the column names are set 
    to lower case. An index of the DataFrame is set to the insurance undertaking name and the reporting period. Then 
    we perform some cleaning (the original worksheets contain some process information). In addition, some worksheets 
    in the file contain 2-dimensional data, that need to be pivoted such that we obtain one large vector with all the 
    data per insurance undertaking in one row.
    
    Parameters:
    num (int): number of the worksheet
    
    Returns: 
    dataframe: cleaned and indexed dataframe with all data per insurance undertaking in one row
    
    """
    
    # read entire Excel sheet
    df = xls.parse(num)

    # columns names to lower case
    df.columns = [c.lower() for c in df.columns]

    # set index to name and period
    df.set_index(['relatienaam', 'periode'], inplace = True)

    # data cleaning (the excel sheet contains some additional data that we don't need)
    drop_list = [i for i in df.columns if 'unnamed' in i or 'selectielijst' in i]
    df.drop(drop_list, axis = 1, inplace = True)
    
    # pivot DataFrame
    if "row_name" in df.columns:
        df.drop("row_name", axis = 1, inplace = True)
        df = df.pivot(columns = 'row_header')

    if df.columns.nlevels > 1:
        df.columns = [str(df.columns[i]) for i in range(len(df.columns))]

    # remove duplicate rows
    df = df[~(df.index.duplicated())]
        
    return df
    