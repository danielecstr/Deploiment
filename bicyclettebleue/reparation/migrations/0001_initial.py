# Generated by Django 3.2.7 on 2021-10-04 14:10

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codename', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
                ('first_name', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CommandeFournisseur',
            fields=[
                ('commande_fourni_id', models.AutoField(db_column='COMMANDE_FOURNI_ID', primary_key=True, serialize=False)),
                ('commadne_fourni_datecommande', models.IntegerField(blank=True, db_column='COMMADNE_FOURNI_DATECOMMANDE', null=True)),
                ('commande_fourni_statut', models.TextField(blank=True, db_column='COMMANDE_FOURNI_STATUT', null=True)),
                ('fourni_id', models.IntegerField(blank=True, db_column='FOURNI_ID', null=True)),
            ],
            options={
                'db_table': 'Commande_fournisseur',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('change_message', models.TextField()),
                ('action_flag', models.PositiveSmallIntegerField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Donateur',
            fields=[
                ('don_id', models.IntegerField(db_column='DON_ID', primary_key=True, serialize=False)),
                ('don_nom', models.TextField(blank=True, db_column='DON_NOM', null=True)),
                ('don_prenom', models.TextField(blank=True, db_column='DON_PRENOM', null=True)),
                ('don_adresseposte', models.TextField(blank=True, db_column='DON_ADRESSEPOSTE', null=True)),
                ('don_npa', models.IntegerField(blank=True, db_column='DON_NPA', null=True)),
                ('don_localite', models.TextField(blank=True, db_column='DON_LOCALITE', null=True)),
                ('don_tel', models.IntegerField(blank=True, db_column='DON_TEL', null=True)),
            ],
            options={
                'db_table': 'Donateur',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EstFourniPar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fourni_id', models.IntegerField(blank=True, db_column='FOURNI_ID', null=True)),
                ('piece_id', models.IntegerField(blank=True, db_column='PIECE_ID', null=True)),
            ],
            options={
                'db_table': 'EST_FOURNI_PAR',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('fourni_id', models.AutoField(db_column='FOURNI_ID', primary_key=True, serialize=False)),
                ('fourni_nom', models.TextField(blank=True, db_column='FOURNI_NOM', null=True)),
                ('fourni_adresseposte', models.TextField(blank=True, db_column='FOURNI_ADRESSEPOSTE', null=True)),
                ('fourni_tel', models.IntegerField(blank=True, db_column='FOURNI_TEL', null=True)),
                ('fourni_npa', models.IntegerField(blank=True, db_column='FOURNI_NPA', null=True)),
                ('fourni_desc', models.TextField(blank=True, db_column='FOURNI_DESC', null=True)),
            ],
            options={
                'db_table': 'Fournisseur',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('local_id', models.AutoField(db_column='LOCAL_ID', primary_key=True, serialize=False)),
                ('local_nom', models.CharField(blank=True, db_column='LOCAL_NOM', max_length=50, null=True)),
                ('local_adresseposte', models.TextField(blank=True, db_column='LOCAL_ADRESSEPOSTE', null=True)),
                ('local_npa', models.IntegerField(blank=True, db_column='LOCAL_NPA', null=True)),
                ('local_capacite', models.IntegerField(blank=True, db_column='LOCAL_CAPACITE', null=True)),
                ('local_nb_velo', models.IntegerField(blank=True, db_column='LOCAL_NB_VELO', null=True)),
            ],
            options={
                'db_table': 'Local',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PieceComandeFourni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite_commande', models.IntegerField(blank=True, db_column='QUANTITE_COMMANDE', null=True)),
                ('pcf_piece_id', models.IntegerField(blank=True, db_column='PCF_PIECE_ID', null=True)),
                ('pcf_commande_fourni_id', models.IntegerField(blank=True, db_column='PCF_COMMANDE_FOURNI_ID', null=True)),
            ],
            options={
                'db_table': 'PIECE_COMANDE_FOURNI',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PieceDeVelo',
            fields=[
                ('piece_id', models.AutoField(db_column='PIECE_ID', primary_key=True, serialize=False)),
                ('piece_num', models.IntegerField(blank=True, db_column='PIECE_NUM', null=True)),
                ('piece_nom', models.IntegerField(blank=True, db_column='PIECE_NOM', null=True)),
                ('piece_type', models.TextField(blank=True, db_column='PIECE_TYPE', null=True)),
                ('piece_marque', models.TextField(blank=True, db_column='PIECE_MARQUE', null=True)),
                ('piece_nb', models.IntegerField(blank=True, db_column='PIECE_NB', null=True)),
            ],
            options={
                'db_table': 'Piece_de_velo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reparation_velos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rep_id', models.IntegerField(blank=True, db_column='REP_ID', null=True)),
                ('rep_date_heure', models.DateField(db_column='REP_DATE_HEURE')),
                ('rep_desc', models.TextField(blank=True, db_column='REP_DESC', null=True)),
            ],
            options={
                'db_table': 'EST_FOURNI_PAR',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Velo',
            fields=[
                ('vel_id', models.AutoField(db_column='VEL_ID', primary_key=True, serialize=False)),
                ('vel_num_cadre', models.IntegerField(db_column='VEL_NUM_CADRE', null=True)),
                ('vel_nom', models.CharField(db_column='VEL_NOM', max_length=100, null=True)),
                ('vel_marque', models.CharField(choices=[('Ridley', 'Ridley'), ('Pinarello', 'Pinarello'), ('De Rosa', 'De Rosa'), ('Cannondale', 'Cannondale'), ('Specialized', 'Specialized'), ('Van Rysel', 'Van Rysel'), ('Eddardo Bianchi', 'Eddardo Bianchi'), ('Look', 'Look')], db_column='VEL_MARQUE', max_length=50, null=True)),
                ('vel_couleur', models.CharField(choices=[('Rouge', 'Rouge'), ('Vert', 'Vert'), ('Bleu', 'Bleue'), ('Jaune', 'Jaune'), ('Violet', 'Violet'), ('Rose', 'Rose'), ('Orange', 'Orange'), ('Cyan', 'Cyan'), ('Brun', 'Brun'), ('Noir', 'Noir'), ('Gris', 'Gris'), ('Nlanc', 'Blanc')], db_column='VEL_COULEUR', max_length=25, null=True)),
                ('vel_type', models.CharField(choices=[('Vélo tout-terrain', 'VTT'), ('Vélo de route', 'Vélo de route'), ('BMX', 'BMX')], db_column='VEL_TYPE', max_length=50, null=True)),
                ('vel_photo', models.ImageField(blank=True, default='Aucune image', upload_to=django.core.files.storage.FileSystemStorage)),
                ('vel_statut', models.CharField(blank=True, choices=[('Libre', 'Libre'), ('Réservation', 'Réservé'), ('Commande', 'En commande'), ('Location', 'En cours de location')], db_column='VEL_STATUT', max_length=100, null=True)),
                ('vel_etat', models.CharField(choices=[('Cassé', 'Cassé'), ('Bon état', 'Bon état')], db_column='VEL_ETAT', max_length=100, null=True)),
                ('vel_remarque', models.TextField(blank=True, db_column='VEL_REMARQUE', null=True)),
            ],
            options={
                'db_table': 'Velo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FileField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.FileField(upload_to='photo_velos/')),
            ],
        ),
    ]
