import pytest
from atproto_identity.did.resolver import DidResolver
from atproto_identity.exceptions import DidNotFoundError, DidWebResolverError, UnsupportedDidWebPathError

# THESE TESTS ARE NOT MOCKED WITH TEST SERVERS. IT PERFORMS REAL REQUESTS TO THE INTERNET.


def test_did_resolver_with_web_feed() -> None:
    feed_url = 'feed.atproto.blue'
    gen_endpoint = f'https://{feed_url}'
    did_web = f'did:web:{feed_url}'

    did_doc = DidResolver().ensure_resolve(did_web)

    assert did_doc.id == did_web
    assert did_doc.get_feed_gen_endpoint() == gen_endpoint


def test_did_resolver_with_invalid_did_web() -> None:
    with pytest.raises(UnsupportedDidWebPathError):
        DidResolver().ensure_resolve('did:web:feed.atproto.blue:lol:kek')


def test_did_resolver_with_unknown_did_web() -> None:
    with pytest.raises(DidWebResolverError):
        DidResolver().ensure_resolve('did:web:feed123.atproto.blue')


def test_did_resolver_with_did_plc() -> None:
    expected_handle = 'test.marshal.dev'
    expected_key_type = 'Multikey'
    expected_did_plc = 'did:plc:kvwvcn5iqfooopmyzvb4qzba'

    did_doc = DidResolver().ensure_resolve(expected_did_plc)

    assert did_doc.id == expected_did_plc
    assert did_doc.get_handle() == expected_handle
    assert did_doc.get_signing_key().type == expected_key_type


def test_did_resolver_with_unknown_did_plc() -> None:
    with pytest.raises(DidNotFoundError):
        did_plc = 'did:plc:kvwvcn5iqfooopmyzvb41234'
        DidResolver().ensure_resolve(did_plc)
