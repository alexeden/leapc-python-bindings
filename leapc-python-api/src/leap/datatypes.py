"""Wrappers for LeapC Data types"""

from typing import Generic, TypeVar
from .cstruct import LeapCStruct
from .enums import HandType
from leapc_cffi import ffi


class FrameData:
    """Wrapper which owns all the data required to read the Frame

    A LEAP_TRACKING_EVENT has a fixed size, but some fields are pointers to memory stored
    outside of the struct. This means the size required for all the information about a
    frame is larger than the size of the struct.

    This wrapper owns the buffer required for all of that data. Reading attributes or
    items from this wrapper returns the corresponding item or wrapper on the underlying
    LEAP_TRACKING_EVENT.

    It is intended to by used in the TrackingEvent constructor.
    """

    def __init__(self, size):
        self._buffer = ffi.new("char[]", size)
        self._frame_ptr = ffi.cast("LEAP_TRACKING_EVENT*", self._buffer)

    def __getattr__(self, name):
        return getattr(self._frame_ptr, name)

    def __getitem__(self, key):
        return self._frame_ptr[key]

    def frame_ptr(self):
        return self._frame_ptr


class FrameHeader(LeapCStruct):
    @property
    def frame_id(self) -> int:
        return self._data.frame_id

    @property
    def timestamp(self):
        return self._data.timestamp


T = TypeVar("T", default=float)


# Make Vector generic over T with default type float
class Vector(LeapCStruct, Generic[T]):
    def __getitem__(self, idx):
        return self._data.v[idx]

    def __iter__(self):
        return [self._data.v[i] for i in range(3)].__iter__()

    @property
    def x(self) -> T:
        return self._data.x

    @property
    def y(self) -> T:
        return self._data.y

    @property
    def z(self) -> T:
        return self._data.z


class Quaternion(LeapCStruct, Generic[T]):
    def __getitem__(self, idx):
        return self._data.v[idx]

    def __iter__(self):
        return [self._data.v[i] for i in range(4)].__iter__()

    @property
    def x(self) -> T:
        return self._data.x

    @property
    def y(self) -> T:
        return self._data.y

    @property
    def z(self) -> T:
        return self._data.z

    @property
    def w(self) -> T:
        return self._data.w


class Palm(LeapCStruct, Generic[T]):
    @property
    def position(self) -> Vector[T]:
        return Vector(self._data.position)

    @property
    def stabilized_position(self) -> Vector[T]:
        return Vector(self._data.stabilized_position)

    @property
    def velocity(self) -> Vector[T]:
        return Vector(self._data.velocity)

    @property
    def normal(self) -> Vector[T]:
        return Vector(self._data.normal)

    @property
    def width(self) -> T:
        return self._data.width

    @property
    def direction(self) -> Vector[T]:
        return Vector(self._data.direction)

    @property
    def orientation(self) -> Quaternion[T]:
        return Quaternion(self._data.orientation)


class Bone(LeapCStruct, Generic[T]):
    @property
    def prev_joint(self) -> Vector[T]:
        return Vector(self._data.prev_joint)

    @property
    def next_joint(self) -> Vector[T]:
        return Vector(self._data.next_joint)

    @property
    def width(self) -> T:
        return self._data.width

    @property
    def rotation(self) -> Quaternion[T]:
        return Quaternion(self._data.rotation)


class Digit(LeapCStruct, Generic[T]):
    @property
    def finger_id(self) -> int:
        return self._data.finger_id

    @property
    def bones(self) -> list[Bone[T]]:
        return [self.metacarpal, self.proximal, self.intermediate, self.distal]

    @property
    def metacarpal(self) -> Bone[T]:
        return Bone(self._data.metacarpal)

    @property
    def proximal(self) -> Bone[T]:
        return Bone(self._data.proximal)

    @property
    def intermediate(self) -> Bone[T]:
        return Bone(self._data.intermediate)

    @property
    def distal(self) -> Bone[T]:
        return Bone(self._data.distal)

    @property
    def is_extended(self) -> bool:
        return self._data.is_extended


class Hand(LeapCStruct, Generic[T]):
    @property
    def id(self) -> int:
        return self._data.id

    @property
    def flags(self):
        return self._data.flags

    @property
    def type(self) -> HandType:
        return HandType(self._data.type)

    @property
    def confidence(self) -> float:
        return self._data.confidence

    @property
    def visible_time(self):
        return self._data.visible_time

    @property
    def pinch_distance(self) -> float:
        return self._data.pinch_distance

    @property
    def grab_angle(self) -> float:
        return self._data.grab_angle

    @property
    def pinch_strength(self) -> float:
        return self._data.pinch_strength

    @property
    def grab_strength(self) -> float:
        return self._data.grab_strength

    @property
    def palm(self) -> Palm[T]:
        return Palm(self._data.palm)

    @property
    def thumb(self) -> Digit[T]:
        return Digit(self._data.thumb)

    @property
    def index(self) -> Digit[T]:
        return Digit(self._data.index)

    @property
    def middle(self) -> Digit[T]:
        return Digit(self._data.middle)

    @property
    def ring(self) -> Digit[T]:
        return Digit(self._data.ring)

    @property
    def pinky(self) -> Digit[T]:
        return Digit(self._data.pinky)

    @property
    def digits(self) -> list[Digit[T]]:
        return [self.thumb, self.index, self.middle, self.ring, self.pinky]

    @property
    def arm(self) -> Bone[T]:
        return Bone(self._data.arm)


class Image(LeapCStruct):
    @property
    def matrix_version(self):
        return self._data.matrix_version
