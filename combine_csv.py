import pandas as pd
import sys
import os

# path to current working directory
PATH = os.path.join(os.getcwd(), 'fixtures')


def create_csv(df):
    df.to_csv(os.path.join(PATH, sys.argv[len(sys.argv)-1]), index=False)
    print(f'New file {sys.argv[len(sys.argv)-1]} saved at location {os.path.join(PATH, sys.argv[len(sys.argv)-1])}')


def get_files():
    '''
    get all of the file paths to the files specified in command line arguments
    and store both the file name and full path

    return two lists, one containing full file paths and one containing file names
    '''
    files = []
    file_names = []
    for i in range(1, len(sys.argv)-1):
        files.append(os.path.join(PATH , str(sys.argv[i].split('/')[2])))
        file_names.append(sys.argv[i].split('/')[2])
    return files, file_names


def create_final_dataframe(files, file_names):
    '''
    create an initial pandas dataframe by reading the first entered file
    add a new column for the filename to the dataframe
    go through the rest of the file arguments, read them into a temporary dataframe, 
    add file name column, concatenate temporary dataframe with what will be the final dataframe

    return a pandas dataframe containing the information from all entered files and a new column
    denoting which file a row came from
    '''
    
    try:
        df = pd.read_csv(files[0])
    except FileNotFoundError:
        print(f'The file {files[0]} does not exist')
    df['filename'] = [file_names[0]]*len(df)

    for i in range(1, len(files)):
        try:
            temp_df = pd.read_csv(files[i])
        except FileNotFoundError:
            print(f'The file {files[i]} does not exist')

        temp_df['filename'] = [file_names[i]]*len(temp_df)
        df = pd.concat([df, temp_df])
    
    print(df)
    return df


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Please enter at least two file names")
    else:
        files, file_names = get_files()
        final_data = create_final_dataframe(files, file_names)
        create_csv(final_data)
