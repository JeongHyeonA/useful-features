import pandas as pd
import os 

# 파일 경로입력 받기
file_path = input('파일경로 입력하세요 : ')
output_path = input('저장할 파일 이름과 확장자를 입력하세요 ex) abc.xlsx : ')

filePath, fileName  = os.path.split(file_path)
output = os.path.join(filePath, output_path)

# 입력받은 파일 열기
file = pd.read_csv(file_path)

# 빈 데이터 프레임 생성
bin_df = pd.DataFrame()

# 데이터 개수 10개 미만 중복값 제거 후 count 
for i in range(len(file.columns)):
    if len(file.iloc[:,i].unique()) < 10 :
        a = file.iloc[:,i].value_counts().to_frame().reset_index()
        a = a.rename(columns={file.columns[i] : file.columns[i]+ 'Counts'})
        a.rename(columns={'index' : file.columns[i]},inplace=True)
        bin_df = pd.concat([bin_df,a],axis= 1)

# 소수점이 생기기 떄문에 빈 값에 특정 int값 넣어주기        
bin_df.fillna(10000, inplace = True)

# 모든 컬럼어 대해 int형 변환 해주기
for i in bin_df.columns:
    if bin_df.dtypes[i] != 'object':
        bin_df[i] = bin_df[i].astype('int64')

# int형 변환 후 특정 int값 넣은 걸 None값으로 교체
bin_df.replace(10000, None, inplace = True)

bin_df.to_excel(output)
