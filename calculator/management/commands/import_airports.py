import csv
from django.core.management.base import BaseCommand
from calculator.models import Airport

class Command(BaseCommand):
    help = "Import airports from a CSV file"

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help="Path to the CSV file")

    def handle(self, *args, **options):
        csv_file = options['csv_file']

        with open(csv_file, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            count = 0

            for row in reader:
                _, created = Airport.objects.get_or_create(
                    iata_code=row['iata_code'],
                    defaults={
                        'name': row['name'],
                        'latitude': float(row['latitude']),
                        'longitude': float(row['longitude']),
                    }
                )
                if created:
                    count += 1

        self.stdout.write(self.style.SUCCESS(f'Successfully imported {count} airports!'))
