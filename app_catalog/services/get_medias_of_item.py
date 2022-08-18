from app_catalog.models import Media


class GetMediasOfItem:
    def _get_cover(self, qs):
        return qs.cover_image

    def _get_additional_pics(self, qs):
        return qs.additional_image.all()

    def execute(self, obj):
        cover = self._get_cover(obj)
        pics = self._get_additional_pics(obj)

        return cover, pics
