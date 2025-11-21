from django.db import models

# Create your models here.
# un model est un objet(ou classe) et qui représente les données dans une table SQL
# exemple l'objet Member représente une personne (table) avec les propriétés
#   - prenom (sera l'intitulé "firstname" d'une colonne dans la table Member)
#   - nom    (sera l'intitulé "lastname" d'une colonne dans la table Member)
#
# la table Member sera créée automatiquement par python
# 
# pour afficher la commande SQL, lancer la commande:
#      python manage.py sqlmigrate members 0001
# pour entrer les données dans la table, utiliser la commande:
#      python manage.py shell

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  date = models.DateField(null=True)

  def __str__(self):
    return f"{self.firstname} {self.lastname}"

