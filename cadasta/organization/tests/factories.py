import factory

from ..models import Organization, OrganizationRole, Project, ProjectRole


class OrganizationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Organization

    name = factory.Sequence(lambda n: "Organization #%s" % n)
    slug = factory.Sequence(lambda n: "organization-%s" % n)
    description = factory.Sequence(
        lambda n: "Organization #%s description" % n)
    urls = ['http://example.com']
    contacts = []

    @factory.post_generation
    def add_users(self, create, users, **kwargs):
        if not create:
            return

        if users:
            for u in users:
                OrganizationRole.objects.create(organization=self, user=u)


class ProjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Project

    name = factory.Sequence(lambda n: "Project #%s" % n)
    organization = factory.SubFactory(OrganizationFactory)
    description = factory.Sequence(
                  lambda n: "Organization #%s description" % n)
    urls = ['http://example.com']
    contacts = []

    @factory.post_generation
    def add_users(self, create, users, **kwargs):
        if not create:
            return

        if users:
            for u in users:
                ProjectRole.objects.create(project=self, user=u)
