# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import api_requestor
from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import DeletableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import SearchableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.abstract import custom_method


@custom_method("delete_discount", http_verb="delete", http_path="discount")
class Subscription(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    SearchableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "subscription"

    @classmethod
    def _cls_cancel(
        cls,
        subscription_exposed_id,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "delete",
            "/v1/subscriptions/{subscription_exposed_id}".format(
                subscription_exposed_id=util.sanitize_id(
                    subscription_exposed_id
                )
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_cancel")
    def cancel(self, idempotency_key=None, **params):
        return self._request(
            "delete",
            "/v1/subscriptions/{subscription_exposed_id}".format(
                subscription_exposed_id=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def search(cls, *args, **kwargs):
        return cls._search(
            search_url="/v1/subscriptions/search", *args, **kwargs
        )

    @classmethod
    def search_auto_paging_iter(cls, *args, **kwargs):
        return cls.search(*args, **kwargs).auto_paging_iter()

    def delete_discount(self, **params):
        requestor = api_requestor.APIRequestor(
            self.api_key,
            api_version=self.stripe_version,
            account=self.stripe_account,
        )
        url = self.instance_url() + "/discount"
        _, api_key = requestor.request("delete", url, params)
        self.refresh_from({"discount": None}, api_key, True)
