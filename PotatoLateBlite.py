# daily average temperature
data['date'] = pd.to_datetime(data['date'])
daily_avg_temp = data.groupby(pd.Grouper(key='date', freq='D'))['temperature'].mean().reset_index()
df_avg_temp = pd.DataFrame(daily_avg_temp, columns=['date', 'avg_temperature'])

grouped_data = data.groupby(pd.Grouper(key='date', freq='D'))
hours = grouped_data.apply(lambda x: len(x[(x['temperature'] > 10) & (x['humidity'] > 90)]))
df_hours = pd.DataFrame({'date': hours.index.date, 'hours': hours.values})

df_merged = pd.merge(df_avg_temp, df_hours, on='date')
df_merged['disease_risk'] = df_merged.apply(lambda row: 0 if (10 <= row['avg_temperature'] <= 23) and (row['hours_condition_met'] > 10) else 1, axis=1)

