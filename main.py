import pandas

# prodi, matkul, kode, nama_matkul, kelas, total peserta kelas, rata-rata mhs hadir
# group by kelas
dataset = pandas.read_csv('dataset1.csv')
columns = ["Prodi" ,"Mata Kuliah", "Kelas"]
groupBy = dataset.groupby(columns)

# get count mahasiswa using [size]
counted = groupBy.size().reset_index(name='total peserta kelas') # type: ignore

# get mean of mhs attendances using [mean]
meanHadir = groupBy["Jml Hadir"].mean().reset_index(name='rata-rata mhs hadir')

# merge data on [columns]
mergeData = pandas.merge(counted, meanHadir, on=columns)
print(mergeData.head())
mergeData.to_excel('result.xlsx', index=False)