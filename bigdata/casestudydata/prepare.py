import pandas as pd

raw = pd.read_csv('/Users/xiewangyi/Downloads/query-hive-256.csv')
raw.sort_values(by=['wayzid', 'clienttime'], inplace=True)
raw = raw.reset_index(drop=True)

current_wayzid = None
start_index = 0
for index, row in raw.iterrows():
    if current_wayzid is None:
        current_wayzid = row['wayzid']
    if current_wayzid != row['wayzid']:
        filtered_data = raw.ix[start_index:index - 1,
                        ['clienttime', 'lon', 'lat', 'lv', 'duration']]
        # if filtered_data.sum()['lv'] < 136:
        #    continue
        print(filtered_data.to_json(orient='values'))
        start_index = index
        current_wayzid = row['wayzid']

filtered_data = raw.ix[start_index:, ['clienttime', 'lon', 'lat', 'lv', 'duration']]
print(filtered_data.to_json(orient='values'))
