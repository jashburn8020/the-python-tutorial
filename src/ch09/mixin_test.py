"""Mixins."""


class GraphicalEntity:
    def __init__(self, size_x: int, size_y: int) -> None:
        self.size_x = size_x
        self.size_y = size_y


class Button(GraphicalEntity):
    def __init__(self, size_x: int, size_y: int) -> None:
        super().__init__(size_x, size_y)
        self.status = False

    def toggle(self) -> bool:
        self.status = not self.status
        return self.status


class LimitSizeMixin:
    """Mixin that limits the size of a `GraphicalEntity` to 500 x 400."""

    def __init__(self, size_x: int, size_y: int) -> None:
        super().__init__(min(size_x, 500), min(size_y, 400))


class LimitSizeButton(LimitSizeMixin, Button):
    """Limited size button."""


def test_normal_button() -> None:
    """Button without mixin to limit its size."""
    button = Button(1000, 500)
    assert button.toggle()
    assert not button.toggle()

    assert (button.size_x, button.size_y) == (1000, 500)


def test_limit_button() -> None:
    """Button with mixin to limit its size."""
    button = LimitSizeButton(1000, 500)
    assert button.toggle()
    assert not button.toggle()

    assert (button.size_x, button.size_y) == (500, 400)

    assert LimitSizeButton.__mro__ == (
        LimitSizeButton,
        LimitSizeMixin,
        Button,
        GraphicalEntity,
        object,
    )
