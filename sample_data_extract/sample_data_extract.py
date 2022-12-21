import pandas as pd
import os

# 파일 경로입력 받기
file_path = input('파일경로 입력하세요 : ')
output_path = input('저장할 파일 이름과 확장자를 입력하세요 ex) abc.xlsx : ')

filePath, fileName  = os.path.split(file_path)
output = os.path.join(filePath, output_path)

# 샘플링 데이터 입력받기
sample_data_count = int(input('샘플링 데이터 개수를 입력해 주세요 : '))

# 청크사이즈 설정
chunksize = 100000

# 빈 데이터 프레임 생성
empty_df = pd.DataFrame()

# 청크사이즈 크기 만큼 sample 데이터 추출 반복
chunksize = 100000
empty_df = pd.DataFrame()
for cnt, chunk in enumerate(pd.read_csv(file_path, encoding = 'utf-8', chunksize= chunksize,low_memory = False)):
    if sample_data_count <= chunksize:
        empty_df = pd.concat([empty_df,chunk.sample(sample_data_count, replace = True)])
        break
    else:
        empty_df = pd.concat([empty_df,chunk.sample(chunksize,replace=True)])
        cha = sample_data_count - len(empty_df)
        if cha <= chunksize :
            empty_df = pd.concat([empty_df,chunk.sample(cha,replace=False)])
            if len(empty_df) == sample_data_count:
                break

# xlsx 형태로 출력
empty_df.to_excel(output)