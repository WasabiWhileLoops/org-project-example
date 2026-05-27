import logging

logger = logging.getLogger(__name__)

def test_math_addition():
    logger.info("Performing dummy test")
    assert 1 + 1 == 2
    

# should fail. testing ci workflow
def test_fail_math_addition():
    logger.info("Performing dummy test that should fail")
    assert 1 + 1 == 3
    