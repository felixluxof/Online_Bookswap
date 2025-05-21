from django.core.management.base import BaseCommand
from books.models import Category, Books
from account.models import CustomUser
from django.utils.text import slugify
from django.core.files.base import ContentFile
from io import BytesIO
from PIL import Image
from decimal import Decimal

class Command(BaseCommand):
    help = 'Инициализация базы книгами'

    def handle(self, *args, **kwargs):
        # Весь ваш код скрипта сюда
        owner = CustomUser.objects.first()

        def generate_dummy_image(name='book'):
            img = Image.new('RGB', (200, 300), color=(120, 120, 200))
            buf = BytesIO()
            img.save(buf, format='JPEG')
            buf.seek(0)
            return ContentFile(buf.read(), name=f'{name}.jpg')

        def get_unique_slug(name):
            base_slug = slugify(name)
            slug = base_slug
            counter = 1
            while Books.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            return slug

        books_data = [
    {
        "genre": "Фэнтези",
        "title": "Властелин колец",
        "description": "Эпическое фэнтези Дж. Р. Р. Толкина о борьбе добра и зла в Средиземье.",
        
    },
    {
        "genre": "Научная фантастика",
        "title": "Дюна",
        "description": "Фрэнк Герберт рассказывает о борьбе за выживание и власть на пустынной планете Арракис.",
        
    },
    {
        "genre": "Детектив",
        "title": "Убийство в «Восточном экспрессе»",
        "description": "Классический детектив Агаты Кристи с Эркюлем Пуаро в главной роли.",
        
    },
    {
        "genre": "Триллер",
        "title": "Девушка с татуировкой дракона",
        "description": "Журналист и хакер раскрывают мрачные семейные тайны. Автор: Стиг Ларссон.",
        
    },
    {
        "genre": "Ужасы",
        "title": "Сияние",
        "description": "Психологический хоррор Стивена Кинга о семье, запертой в проклятом отеле.",
        
    },
    {
        "genre": "Любовный роман",
        "title": "Гордость и предубеждение",
        "description": "Классика Джейн Остин о любви, статусе и предрассудках.",
        
    },
    {
        "genre": "Современная проза",
        "title": "Нормальные люди",
        "description": "Салли Руни исследует сложные отношения между двумя молодыми людьми.",
        
    },
    {
        "genre": "Классика",
        "title": "Преступление и наказание",
        "description": "Ф.М. Достоевский — психологический роман о вине, раскаянии и искуплении.",
        
    },
    {
        "genre": "Молодёжная литература",
        "title": "Виноваты звёзды",
        "description": "Джон Грин о любви и жизни подростков с раком.",
        
    },  {
        "genre": "Приключения",
        "title": "Остров сокровищ",
        "description": "Классика Роберта Льюиса Стивенсона о пиратских приключениях и кладах.",
        
    },
    {
        "genre": "Биография / автобиография",
        "title": "Стив Джобс",
        "description": "Официальная биография Стива Джобса, написанная Уолтером Айзексоном.",
        
    },
    {
        "genre": "Саморазвитие",
        "title": "Семь навыков высокоэффективных людей",
        "description": "Стивен Кови — культовое руководство по личной эффективности.",
        
    },
    {
        "genre": "Психология",
        "title": "Думай медленно... решай быстро",
        "description": "Даниэль Канеман — нобелевский лауреат о работе нашего мышления.",
        
    },
    {
        "genre": "Исторический роман",
        "title": "Война и мир",
        "description": "Эпопея Льва Толстого о России начала XIX века, любви, войне и судьбе.",
        
    },
    {
        "genre": "Постапокалипсис / антиутопия",
        "title": "1984",
        "description": "Джордж Оруэлл описывает тоталитарное общество, где за каждым следят.",
        
    }
]


        for book in books_data:
            genre_name = book["genre"]
            category, _ = Category.objects.get_or_create(
                name=genre_name,
                slug=slugify(genre_name),
                defaults={"is_active": True}
            )

            slug = get_unique_slug(book["title"])

            book_obj, created = Books.objects.get_or_create(
                slug=slug,
                defaults={
                    'name': book["title"],
                    'description': book["description"],
                    'is_active': True,
                    'owner': owner,
                }
            )

            if created:
                image_file = generate_dummy_image(slug)
                book_obj.photo.save(image_file.name, image_file, save=True)

                content_file = ContentFile(b"Demo book content", name=f"{slug}.pdf")
                book_obj.file.save(content_file.name, content_file, save=True)

                book_obj.save()

        self.stdout.write(self.style.SUCCESS('Книги успешно инициализированы!'))
