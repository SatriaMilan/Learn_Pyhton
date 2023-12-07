from functools import reduce

movies = [
    {"title": "Avengers: Endgame", "year": 2019, "rating": 8.4, "genre": "Action"},
    {"title": "Parasite", "year": 2019, "rating": 8.6, "genre": "Drama"},
    {"title": "Nomadland", "year": 2020, "rating": 7.3, "genre": "Drama"},
    {"title": "Dune", "year": 2021, "rating": 7.9, "genre": "Sci-Fi"},
    {"title": "Spider-man: No Way Home", "year": 2021, "rating": 7.6, "genre": "Action"},
    {"title": "The French Dispatch", "year": 2021, "rating": 7.0, "genre": "Comedy"},
    {"title": "A Quiet Place Part II", "year": 2020, "rating": 7.4, "genre": "Horror"},
    {"title": "No Time to Die", "year": 2021, "rating": 6.8, "genre": "Action"},
    {"title": "The Power of the Dog", "year": 2021, "rating": 7.3, "genre": "Drama"},
    {"title": "Eternals", "year": 2021, "rating": 6.4, "genre": "Action"},
    {"title": "The Last Duel", "year": 2021, "rating": 7.0, "genre": "Drama"},
]

def display_movie_data(movie):
    print("Judul Film:", movie["title"])
    print("Tahun Rilis:", movie["year"])
    print("Rating:", movie["rating"])
    print("Genre:", movie["genre"])

def filter_movies_by_genre(genre):
    filtered_movies = filter(lambda movie: movie["genre"].lower() == genre.lower(), movies)
    return list(filtered_movies)

def map_ratings():
    return list(map(lambda movie: movie["rating"], movies))

def calculate_average_rating(ratings):
    total = reduce(lambda x, y: x + y, ratings)
    return total / len(ratings)

def count_movies_by_genre():
    genre_count = {}
    for movie in movies:
        genre = movie["genre"].lower()
        genre_count[genre] = genre_count.get(genre, 0) + 1
    return genre_count

def calculate_average_rating_by_year():
    rating_sum_by_year = {}
    rating_count_by_year = {}
    
    for movie in movies:
        year = movie["year"]
        rating = movie["rating"]
        
        if year in rating_sum_by_year:
            rating_sum_by_year[year] += rating
            rating_count_by_year[year] += 1
        else:
            rating_sum_by_year[year] = rating
            rating_count_by_year[year] = 1

    average_rating_by_year = {year: rating_sum_by_year[year] / rating_count_by_year[year] for year in rating_sum_by_year}
    return average_rating_by_year

def find_highest_rated_movie():
    highest_rated_movie = max(movies, key=lambda movie: movie["rating"])
    return highest_rated_movie

def find_movie_by_title(title):
    for movie in movies:
        if movie["title"].lower() == title.lower():
            return movie
    return None

while True:
    print("Pilih tugas yang ingin dilakukan:")
    print("1. Menghitung jumlah film berdasarkan genre")
    print("2. Menghitung rata-rata rating film berdasarkan tahun rilis")
    print("3. Menemukan film dengan rating tertinggi")
    print("4. Cari judul film untuk menampilkan informasi rating, tahun rilis, dan genre")
    print("5. Selesai")
    
    choice = input("Masukkan nomor tugas (1/2/3/4/5): ")
    
    if choice == "1":
        genre_count = count_movies_by_genre()
        print("Jumlah film berdasarkan genre:")
        print(genre_count)
        print()
    elif choice == "2":
        average_rating_by_year = calculate_average_rating_by_year()
        print("Rata-Rata Rating Film Berdasarkan Tahun Rilis:")
        print(average_rating_by_year)
        print()
    elif choice == "3":
        highest_rated_movie = find_highest_rated_movie()
        print("Film Dengan Rating Tertinggi:")
        display_movie_data(highest_rated_movie)
        print()
    elif choice == "4":
        title = input("Masukkan judul film yang ingin dicari: ")
        found = False
        for movie in movies:
            if movie["title"].lower() == title.lower():
                print("Informasi Film:", movie["title"])
                display_movie_data(movie)
                print()
                found = True
                break
        if not found:
            print("Film tidak ditemukan.")
            print()
    elif choice == "5":
        print("Terimakasih Telah Menggunakan Sistem Ini")
        print("\n\n\n")
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan nomor tugas yang valid.")
        print() 