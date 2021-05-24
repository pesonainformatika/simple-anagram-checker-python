from typing import List
kalimats = 'ant magenta magnate tan gnamate'


def anagram_counter(kalimat: str) -> int:
    counter = 0
    data_str = kalimat.split()
    for data in range(len(data_str)):
        data_str[data] = ''.join(sorted(data_str[data]))

    for count in set(data_str):
        temp = data_str.count(count)
        result = max(counter, temp)

        return result


# cetak ke layar untuk mengetahui jumlah anagram dari suatu kalimat
print(f"{anagram_counter(kalimats)}")

def main():
    data_kata: List = ['William Shakespeare', 'Vladimir Nabokov', 'Anna Madrigal', 'Purwakarta']
    for index, data in enumerate(data_kata, 1):
        print(f"menghitung Jumlah Analisa dari kata ke {index}")
        print(f"Anagram terbanyak yang terbentuk didalam {data} adalah {anagram_counter(kalimat=data)}")



if __name__ == '__main__':
    main()