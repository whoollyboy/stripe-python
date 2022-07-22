# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import custom_method


@custom_method("list_line_items", http_verb="get", http_path="line_items")
class QuotePhase(ListableAPIResource):
    OBJECT_NAME = "quote_phase"

    def list_line_items(self, idempotency_key=None, **params):
        url = "/v1/quote_phases/{quote_phase}/line_items".format(
            quote_phase=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        resp = self.request("get", url, params, headers)
        stripe_object = util.convert_to_stripe_object(resp)
        stripe_object._retrieve_params = params
        return stripe_object