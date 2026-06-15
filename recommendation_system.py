import argparse

movies = {
	'El Padrino': 'Crimen',
	'La La Land': 'Musical',
	'Toy Story': 'Animación',
	'Inception': 'Ciencia ficción',
	'Amélie': 'Romance',
}


def recommend(genre: str) -> None:
	genre_norm = genre.strip().lower()
	matches = [title for title, g in movies.items() if g.lower() == genre_norm]
	if matches:
		print(f"Películas del género '{genre.strip()}':")
		for t in matches:
			print(f"- {t}")
	else:
		print(f"No se encontraron películas del género '{genre.strip()}'.")


def main() -> None:
	parser = argparse.ArgumentParser(description='Sistema de recomendación de películas simple')
	parser.add_argument('--genre', '-g', help='Género de película (p. ej. Crimen, Musical)', default=None)
	args = parser.parse_args()

	if args.genre:
		recommend(args.genre)
	else:
		try:
			genre = input('Introduce un género: ')
		except EOFError:
			genre = ''
		if genre:
			recommend(genre)
		else:
			print('No se proporcionó ningún género. Saliendo.')


if __name__ == '__main__':
	main()