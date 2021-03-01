from django.contrib.auth.models import User
from django.db import models


class ProviderQuerySet(models.QuerySet):
    def search(self, **kwargs):
        qs = self
        if kwargs.get('name', ''):
            qs = qs.filter(name__icontains=kwargs['name'])
        if kwargs.get('description', ''):
            qs = qs.filter(description__contains=kwargs['description'])
        if kwargs.get('services', []):
            qs = qs.filter(services__pk__in=kwargs['services'])
        return qs


class Provider(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=1024)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='static/photos/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to="static/thumbnails/", blank=True, null=True)

    objects = ProviderQuerySet.as_manager()

    # def save(self, *args, **kwargs):
    #     size = (256,256)
    #     if not self.id and not self.photo:
    #         return
    #
    #     try:
    #         old_obj = Provider.objects.get(pk=self.pk)
    #         old_path = old_obj.photo.path
    #     except:
    #         pass
    #
    #     thumb_update = False
    #     if self.thumbnail:
    #         try:
    #             statinfo1 = os.stat(self.photo.path)
    #             statinfo2 = os.stat(self.thumbnail.path)
    #             if statinfo1 > statinfo2:
    #                 thumb_update = True
    #         except:
    #             thumb_update = True
    #
    #     pw = self.photo.width
    #     ph = self.photo.height
    #     nw = size[0]
    #     nh = size[1]
    #
    #     if self.photo and not self.thumbnail or thumb_update:
    #         # only do this if the image needs resizing
    #         if (pw, ph) != (nw, nh):
    #             filename = str(self.photo.path)
    #             image = Image.open(filename)
    #             pr = float(pw) / float(ph)
    #             nr = float(nw) / float(nh)
    #
    #             if image.mode not in ('L', 'RGB'):
    #                 image = image.convert('RGB')
    #
    #             if pr > nr:
    #                 # photo aspect is wider than destination ratio
    #                 tw = int(round(nh * pr))
    #                 image = image.resize((tw, nh), Image.ANTIALIAS)
    #                 l = int(round(( tw - nw ) / 2.0))
    #                 image = image.crop((l, 0, l + nw, nh))
    #             elif pr < nr:
    #                 # photo aspect is taller than destination ratio
    #                 th = int(round(nw / pr))
    #                 image = image.resize((nw, th), Image.ANTIALIAS)
    #                 t = int(round(( th - nh ) / 2.0))
    #                 image = image.crop((0, t, nw, t + nh))
    #             else:
    #                 # photo aspect matches the destination ratio
    #                 image = image.resize(size, Image.ANTIALIAS)
    #
    #         image.save(self.get_thumbnail_path())
    #         (a, b) = os.path.split(self.photo.name)
    #         self.thumbnail = a + '/thumbs/' + b
    #         super(Provider, self).save()
    #         try:
    #             os.remove(old_path)
    #             os.remove(self.get_old_thumbnail_path(old_path))
    #         except:
    #             pass

    # def get_thumbnail_path(self):
    #     (head, tail) = os.path.split(self.photo.path)
    #     if not os.path.isdir(head + '/thumbs'):
    #         os.mkdir(head + '/thumbs')
    #     return head + '/thumbs/' + tail

    # @staticmethod
    # def get_old_thumbnail_path(self, old_photo_path):
    #     (head, tail) = os.path.split(old_photo_path)
    #     return head + '/thumbs/' + tail

    def __str__(self):
        return f"{self.name}"
