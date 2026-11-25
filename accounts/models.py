from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models

class CustomUser(AbstractUser):
    YEARS = [
        ("", "No year selected"),
        ("Freshman", "Freshman"),
        ("Sophmore", "Sophmore"),
        ("Junior", "Junior"),
        ("Senior", "Senior"),
    ]

    MAJORS_BY_TYPE = {
        "BA": ["Math", "Visual Arts", "Sculpting"],
        "BS": ["Computer Science", "Forestry", "Astronomy"],
    }

    MAJOR_TYPES = [("", "Select a major type")] + [
        (m_type, m_type) for m_type in MAJORS_BY_TYPE.keys()
    ]

    MAJORS = [("", "Select a major")] + [
        (major, major)
        for majors in MAJORS_BY_TYPE.values()
        for major in majors
    ]

    INTERESTS = [
        ("Archery", "Archery"),
        ("Arts & Crafts", "Arts & Crafts"),
        ("Badminton", "Badminton"),
        ("Baseball", "Baseball"),
        ("Basketball", "Basketball"),
        ("Bowling", "Bowling"),
        ("Boxing", "Boxing"),
        ("Choir", "Choir"),
        ("Club Sports", "Club Sports"),
        ("Collegiate Sports", "Collegiate Sports"),
        ("Cooking", "Cooking"),
        ("Crochet", "Crochet"),
        ("Dance", "Dance"),
        ("Drawing", "Drawing"),
        ("Football", "Football"),
        ("Gaming", "Gaming"),
        ("Golf", "Golf"),
        ("Ice Skating", "Ice Skating"),
        ("Kickboxing", "Kickboxing"),
        ("Knitting", "Knitting"),
        ("MMA", "MMA"),
        ("Music", "Music"),
        ("Painting", "Painting"),
        ("Pickleball", "Pickleball"),
        ("Pottery", "Pottery"),
        ("Quilting", "Quilting"),
        ("Reading", "Reading"),
        ("Roller Skating", "Roller Skating"),
        ("Running", "Running"),
        ("Sculpting", "Sculpting"),
        ("Sewing", "Sewing"),
        ("Skateboarding", "Skateboarding"),
        ("Soccer", "Soccer"),
        ("Swimming", "Swimming"),
        ("Table Tennis", "Table Tennis"),
        ("Tennis", "Tennis"),
        ("Volleyball", "Volleyball"),
        ("Watercolor", "Watercolor"),
        ("Weight Lifting", "Weight Lifting"),
        ("Wrestling", "Wrestling"),
        ("Yoga", "Yoga"),
        
    ]
    
    MINORS = [
        ("African-American Studies", "African-American Studies"),
        ("Big Data Analytics", "Big Data Analytics"),
        ("Biology", "Biology"),
        ("Business Administration", "Business Administration"),
        ("Central and Southwest Asian Studies", "Central and Southwest Asian Studies"),
        ("Chemistry", "Chemistry"),
        ("Chinese", "Chinese"),
        ("Classical Civilization", "Classical Civilization"),
        ("Classics", "Classics"),
        ("Climate Change Studies", "Climate Change Studies"),
        ("Communication Studies", "Communication Studies"),
        ("Computer Science", "Computer Science"),
        ("Democracy Studies", "Democracy Studies"),
        ("Ecological Restoration", "Ecological Restoration"),
        ("English", "English"),
        ("English Teaching", "English Teaching"),
        ("Environmental Studies", "Environmental Studies"),
        ("Fire Sciences", "Fire Sciences"),
        ("French", "French"),
        ("Geography", "Geography"),
        ("Geosciences", "Geosciences"),
        ("German", "German"),
        ("Global Humanities and Religions", "Global Humanities and Religions"),
        ("History", "History"),
        ("Human and Family Development", "Human and Family Development"),
        ("Irish Studies", "Irish Studies"),
        ("Japanese", "Japanese"),
        ("Latin American Studies", "Latin American Studies"),
        ("Linguistics", "Linguistics"),
        ("Mathematics", "Mathematics"),
        ("Media Arts", "Media Arts"),
        ("Microbiology", "Microbiology"),
        ("Military Studies", "Military Studies"),
        ("Mountain Studies", "Mountain Studies"),
        ("Music", "Music"),
        ("Musical Theatre Performance", "Musical Theatre Performance"),
        ("Native American Studies", "Native American Studies"),
        ("Neuroscience", "Neuroscience"),
        ("Physics", "Physics"),
        ("Russian", "Russian"),
        ("Spanish", "Spanish"),
        ("Sport Psychology", "Sport Psychology"),
        ("Wilderness Studies", "Wilderness Studies"),
        ("Wildlife Biology", "Wildlife Biology"),
        ("Women's Gender and Sexuality Studies", "Women's Gender and Sexuality Studies"),
        ("World Languages and Cultures", "World Languages and Cultures"),
    ]

    CERTIFICATES = [
        ("Accounting Fundamentals", "Accounting Fundamentals"),
        ("Addiction Counseling", "Addiction Counseling"),
        ("Athletic Injury", "Athletic Injury"),
        ("Big Data Analytics", "Big Data Analytics"),
        ("Brewing Science", "Brewing Science"),
        ("Carpentry", "Carpentry"),
        ("Ceramics", "Ceramics"),
        ("Chemical Pharmacology", "Chemical Pharmacology"),
        ("Clinical Medical Assistant", "Clinical Medical Assistant"),
        ("Computer Programming", "Computer Programming"),
        ("Creative Coding", "Creative Coding"),
        ("Creative Entrepreneurship", "Creative Entrepreneurship"),
        ("Cybersecurity", "Cybersecurity"),
        ("Cybersecurity Management", "Cybersecurity Management"),
        ("Dance Wellness", "Dance Wellness"),
        ("Digital & Graphic Design", "Digital & Graphic Design"),
        ("Digital Marketing", "Digital Marketing"),
        ("Documentary Film", "Documentary Film"),
        ("Entertainment Management", "Entertainment Management"),
        ("Entrepreneurship and New Venture Creation", "Entrepreneurship and New Venture Creation"),
        ("Environmental and Nature Writing", "Environmental and Nature Writing"),
        ("Environmental Justice", "Environmental Justice"),
        ("Esports", "Esports"),
        ("Finance Data Analytics", "Finance Data Analytics"),
        ("Game Design", "Game Design"),
        ("General Studies", "General Studies"),
        ("Geographic Information Systems (GIS)", "Geographic Information Systems (GIS)"),
        ("Health Communication", "Health Communication"),
        ("Historic Preservation", "Historic Preservation"),
        ("History of Religions", "History of Religions"),
        ("Human-Centered AI", "Human-Centered AI"),
        ("Indigenous Knowledge and Environmental Sustainability", "Indigenous Knowledge and Environmental Sustainability"),
        ("Information and Control Assurance (ICA)", "Information and Control Assurance (ICA)"),
        ("Interactive Art and Media", "Interactive Art and Media"),
        ("Jazz Studies", "Jazz Studies"),
        ("Language, Regional Expertise, and Culture", "Language, Regional Expertise, and Culture"),
        ("Legal Studies", "Legal Studies"),
        ("LGBTIQ+ Studies", "LGBTIQ+ Studies"),
        ("Logistics & Supply Chain Management", "Logistics & Supply Chain Management"),
        ("Medical Claims Specialist", "Medical Claims Specialist"),
        ("Medical Reception", "Medical Reception"),
        ("Nonprofit Administration", "Nonprofit Administration"),
        ("Northern Rockies Outdoor Leadership", "Northern Rockies Outdoor Leadership"),
        ("Photography and Digital Imaging", "Photography and Digital Imaging"),
        ("Public History", "Public History"),
        ("Reading Education", "Reading Education"),
        ("Social Media and Audience Engagement", "Social Media and Audience Engagement"),
        ("Sound Production Fundamentals", "Sound Production Fundamentals"),
        ("Special Education", "Special Education"),
        ("Specialized Interventionists for Montana Schools", "Specialized Interventionists for Montana Schools"),
        ("Sustainable Agriculture and Food Systems", "Sustainable Agriculture and Food Systems"),
        ("Sustainable Business Strategy", "Sustainable Business Strategy"),
        ("Teaching and Learning - Secondary/K12 Education", "Teaching and Learning - Secondary/K12 Education"),
        ("Water Science and Society", "Water Science and Society"),
        ("Web Design", "Web Design"),
    ]


    
    
    year = models.CharField(max_length=20, choices=YEARS, null=True)
    display_name = models.CharField(max_length=100)
    birthday = models.DateField(null=True)
    age = models.PositiveIntegerField(null=True)
    major_type = models.CharField( max_length=50, choices=MAJOR_TYPES, blank=True, default="")
    major = models.CharField(max_length=100, choices=MAJORS, blank=True, default="")
    interests = models.JSONField(default=list, blank=True)
    bio = models.CharField(max_length=150, null=True)
    minor = models.JSONField(default=list, blank=True)
    certificate = models.JSONField(default=list, blank=True)
    profile_pic = models.ImageField(upload_to="profile_pics/", null=True, blank=True, default="/defaults/profile_pic_default.png")

    def clean(self):
        super().clean()
        if self.major and not self.major_type:
            raise ValidationError({"major": "Select a major type first."})
        if self.major_type and self.major:
            valid_majors = self.MAJORS_BY_TYPE.get(self.major_type, [])
            if self.major not in valid_majors:
                raise ValidationError(
                    {"major": f"{self.major} is not valid for {self.major_type}."}
                )



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
