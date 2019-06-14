from __future__ import absolute_import, division, print_function

import json
from decimal import Decimal

import stripe


TEST_RESOURCE_ID = "250FF"


class TestPlan(object):
    def test_is_listable(self, request_mock):
        resources = stripe.Plan.list()
        request_mock.assert_requested("get", "/v1/plans")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Plan)

    def test_is_retrievable(self, request_mock):
        resource = stripe.Plan.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested("get", "/v1/plans/%s" % TEST_RESOURCE_ID)
        assert isinstance(resource, stripe.Plan)

    def test_is_creatable(self, request_mock):
        resource = stripe.Plan.create(
            amount=100,
            currency="usd",
            id="plan_id",
            interval="month",
            nickname="plan_nickname",
        )
        request_mock.assert_requested("post", "/v1/plans")
        assert isinstance(resource, stripe.Plan)

    def test_is_saveable(self, request_mock):
        resource = stripe.Plan.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        request_mock.assert_requested(
            "post", "/v1/plans/%s" % TEST_RESOURCE_ID
        )

    def test_is_modifiable(self, request_mock):
        resource = stripe.Plan.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/v1/plans/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Plan)

    def test_is_deletable(self, request_mock):
        resource = stripe.Plan.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            "delete", "/v1/plans/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    def test_can_delete(self, request_mock):
        resource = stripe.Plan.delete(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "delete", "/v1/plans/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    def test_deserialize_decimal_string_as_string(self):
        plan = stripe.Plan.construct_from(
            json.loads('{"amount_precise": "0.000000123"}'), stripe.api_key
        )
        assert plan is not None
        assert plan.amount_precise is not None
        assert isinstance(plan.amount_precise, stripe.six.text_type)
        assert plan.amount_precise == "0.000000123"

    class PlanWithAccessor(stripe.Plan):
        @property
        def amount_precise(self):
            return Decimal(self["amount_precise"])

    def test_deserialize_decimal_string_as_decimal(self):
        plan = TestPlan.PlanWithAccessor.construct_from(
            json.loads('{"amount_precise": "0.000000123"}'), stripe.api_key
        )
        assert plan is not None
        assert plan.amount_precise is not None
        print(type(plan.amount_precise))
        assert isinstance(plan.amount_precise, Decimal)
        assert plan.amount_precise == Decimal("0.000000123")
