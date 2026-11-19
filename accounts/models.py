from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    display_name = models.CharField(max_length=100)
    birthday = models.DateField(null=True)
    age = models.PositiveIntegerField(null=True)



class ConnectionType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name



class StudentProfile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="student_profile"
    )
    looking_for = models.ManyToManyField(
        ConnectionType,
        blank=True
)

    display_name = models.CharField(max_length=100)
    major = models.CharField(max_length=100, blank=True)
    graduation_year = models.PositiveIntegerField(null=True, blank=True)
    bio = models.TextField(blank=True)
    interests = models.TextField(blank=True)

    def __str__(self):
        return self.display_name


class Connection(models.Model):
    sender = models.ForeignKey(
        StudentProfile, #model to connect to
        on_delete=models.CASCADE, #delete connection if profile is deleted
        related_name="sent_connections", #retrieve all requests by certain student
    )

    receiver = models.ForeignKey(
        StudentProfile,
        on_delete=models.CASCADE,
        related_name="received_connections",
    )

    class Status(models.TextChoices):
            PENDING = "pending", "Pending"
            ACCEPTED = "accepted", "Accepted"
            REJECTED = "rejected", "Rejected"
            DISCONNECTED = "disconnected", "Disconnected"
            WITHDRAWN = "withdrawn", "Withdrawn"

    status = models.CharField(
            max_length=20,
            choices=Status.choices,
            default=Status.PENDING
        )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )





class Block(models.Model):
    blocker = models.ForeignKey(
        StudentProfile,
        on_delete=models.CASCADE,
        related_name="blocker_connections"
    )

    blockee = models.ForeignKey(
        StudentProfile,
        on_delete=models.CASCADE,
        related_name="blockee_connections"
    )

#blocker and blockee realtions that sets boundaries for who blocks who. Also does not allow user to block themselves in the offchance.
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["blocker", "blockee"],
                name="unique_student_block"
            ),
            models.CheckConstraint(
                check=~models.Q(blocker=models.F("blockee")),
                name="prevent_self_block"
            )
        ]
