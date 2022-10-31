from typing import TypeAlias, Union

JsonValue: TypeAlias = Union[None, bool, int, float, str, "JsonArray", "JsonObject"]
JsonArray: TypeAlias = list[JsonValue]
JsonObject: TypeAlias = dict[str, JsonValue]
