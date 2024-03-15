class ActiveUrlMixin:
    active_url: str | None = None
    active_url_key = "active_url"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs) | {self.active_url_key: self.active_url}
