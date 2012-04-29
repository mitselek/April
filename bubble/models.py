from django.db import models


class BubbleDefinition(models.Model):
    label                   = models.CharField(max_length = 450)
    label_plural            = models.CharField(max_length = 450)
    description             = models.CharField(max_length = 450)
    displayname_definition  = models.CharField(max_length = 450)
    displayinfo_definition  = models.CharField(max_length = 450)
    displaytable_definition = models.CharField(max_length = 450)
    allowed_subtypes        = models.ForeignKey('self', null = True, blank = True, default = None)

    def __unicode__(self):
        return self.label


class Bubble(models.Model):
    bubble_definition = models.ForeignKey(BubbleDefinition)
    relationships     = models.ManyToManyField('self', through = 'Relationship',
                                                symmetrical    = False,
                                                related_name   = 'related_to')
    def __unicode__(self):
        return self.bubble_definition.label

    def relate(self, bubble, relationship, mutual = False):
        relationship, created = Relationship.objects.get_or_create(
            bubble         = self,
            related_bubble = bubble,
            relationship   = relationship)
        if mutual:
            relationship, created = Relationship.objects.get_or_create(
                bubble            = bubble,
                related_bubble    = self,
                relationship      = relationship)
        return relationship

    def unrelate(self, bubble, relationship, mutual = False):
        Relationship.objects.filter(
            bubble         = self,
            related_bubble = bubble,
            relationship   = relationship).delete()
        if mutual:
            Relationship.objects.filter(
                bubble         = bubble,
                related_bubble = self,
                relationship   = relationship).delete()
        return

    def get_relationships(self, relationship):
        return self.relationships.filter(
            related_bubble__relationship = relationship,
            related_bubble__bubble       = self)

    def get_related_to(self, relationship):
        return self.related_to.filter(
            bubble__relationship   = relationship,
            bubble__related_bubble = self)

    def get_subbubbles(self):
        return self.get_relationships(RELATIONSHIP_SUBBUBBLE)

    def get_capsules(self):
        return self.get_related_to(RELATIONSHIP_SUBBUBBLE)

    def get_nextinlines(self):
        return self.get_relationships(RELATIONSHIP_NEXTINLINE)

    def get_previnlines(self):
        return self.get_related_to(RELATIONSHIP_NEXTINLINE)

    def get_prerequisites(self):
        return self.get_relationships(RELATIONSHIP_PREREQUISITE)

    def get_postrequisites(self):
        return self.get_related_to(RELATIONSHIP_PREREQUISITE)


RELATIONSHIP_SUBBUBBLE        = 1
RELATIONSHIP_NEXTINLINE       = 2
RELATIONSHIP_PREREQUISITE     = 3
RELATIONSHIP_RELATED_DOCUMENT = 4
RELATIONSHIPS = (
    (RELATIONSHIP_SUBBUBBLE,        'Subbubble'),
    (RELATIONSHIP_NEXTINLINE,       'Next in line'),
    (RELATIONSHIP_PREREQUISITE,     'Prerequisite'),
    (RELATIONSHIP_RELATED_DOCUMENT, 'Related document'),
)


class Relationship(models.Model):
    bubble         = models.ForeignKey(Bubble, related_name = 'bubbles')
    related_bubble = models.ForeignKey(Bubble, related_name = 'related_bubbles')
    relationship   = models.IntegerField(choices = RELATIONSHIPS)

    def __unicode__(self):
        return RELATIONSHIPS[self.relationship] + ':' + bubble + '&' + related_bubble


class BubblePropertyDefinition(models.Model):
    label                           = models.CharField(max_length = 450)
    label_plural                    = models.CharField(max_length = 450)
    description                     = models.CharField(max_length = 450)
    data_type                       = models.CharField(max_length = 450)
    classifying_bubble_definition   = models.ForeignKey(BubbleDefinition)
    multiplicity                    = models.IntegerField()


class BubbleProperty(models.Model):
    bubble_property_definition  = models.ForeignKey(BubblePropertyDefinition)
    bubble                      = models.ForeignKey(Bubble)
    value_string                = models.CharField(max_length = 450)
    value_integer               = models.IntegerField()
    language                    = models.CharField(max_length = 3)
    data_type                   = models.CharField(max_length = 450)
