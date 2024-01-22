from pydantic import BaseModel, Field, field_validator
from kerykeion.kr_types.settings_models import KerykeionChartSettingsModel
from typing import Optional, Literal
from pytz import all_timezones


class SubjectModel(BaseModel):
    """
    Represents the astrological data for a specific subject.

    Args:
        name (str): Name of the astrological data.
        year (int): Year of the astrological data.
        month (int): Month of the astrological data.
        day (int): Day of the astrological data.
        hour (int): Hour of the astrological data.
        minute (int): Minute of the astrological data.
        city (str, optional): City for which the astrological data is calculated.
        nation (str, optional): Nation for which the astrological data is calculated.
        lng (float, optional): Longitude of the location for which the astrological data is calculated.
        lat (float, optional): Latitude of the location for which the astrological data is calculated.
        tz_str (str): Time zone string for the location for which the astrological data is calculated.
        zodiac_type (str): Type of zodiac used (Tropic or Sidereal).

    Attributes:
        name: Name of the astrological data.
        year: Year of the astrological data.
        month: Month of the astrological data.
        day: Day of the astrological data.
        hour: Hour of the astrological data.
        minute: Minute of the astrological data.
        city: City for which the astrological data is calculated.
        nation: Nation for which the astrological data is calculated.
        lng: Longitude of the location for which the astrological data is calculated.
        lat: Latitude of the location for which the astrological data is calculated.
        tz_str: Time zone string for the location for which the astrological data is calculated.
        zodiac_type: Type of zodiac used (Tropic or Sidereal).

    Raises:
        ValueError: If zodiac_type is not either 'Tropic' or 'Sidereal'.
    """

    name: str = Field(description="The name of the person to get the Birth Chart for.", examples=["John Doe"])
    year: int = Field(description="The year of birth.", examples=[1980])
    month: int = Field(description="The month of birth.", examples=[12])
    day: int = Field(description="The day of birth.", examples=[12])
    hour: int = Field(description="The hour of birth.", examples=[12])
    minute: int = Field(description="The minute of birth.", examples=[12])
    longitude: float = Field(description="The longitude of the birth location. Defaults on London.", examples=[0])
    latitude: float = Field(description="The latitude of the birth location. Defaults on London.", examples=[51.4825766])
    city: str = Field(description="The name of city of birth.", examples=["London"])
    timezone: str = Field(description="The timezone of the birth location.", examples=["Europe/London"])
    zodiac_type: Optional[str] = Field(default="Tropic", description="The type of zodiac used (Tropic or Sidereal).", examples=["Tropic"])

    @field_validator("zodiac_type")
    def validate_zodiac_type(cls, value):
        if value not in ("Tropic", "Sidereal"):
            raise ValueError(f"Invalid zodiac_type '{value}'. Please use either 'Tropic' or 'Sidereal'.")
        return value

    @field_validator("longitude")
    def validate_longitude(cls, value):
        if value < -180 or value > 180:
            raise ValueError(f"Invalid longitude '{value}'. Please use a value between -180 and 180.")
        return value

    @field_validator("latitude")
    def validate_latitude(cls, value):
        if value < -90 or value > 90:
            raise ValueError(f"Invalid latitude '{value}'. Please use a value between -90 and 90.")
        return value

    @field_validator("timezone")
    def validate_timezone(cls, value):
        if value not in all_timezones:
            raise ValueError(f"Invalid timezone '{value}'. Please use a valid timezone.")
        return value

    @field_validator("month")
    def validate_month(cls, value):
        if value < 1 or value > 12:
            raise ValueError(f"Invalid month '{value}'. Please use a value between 1 and 12.")
        return value

    @field_validator("day")
    def validate_day(cls, value, values):
        month = values.data["month"]
        if month in [1, 3, 5, 7, 8, 10, 12]:
            if value < 1 or value > 31:
                raise ValueError(f"Invalid day '{value}'. Please use a value between 1 and 31.")
        elif month in [4, 6, 9, 11]:
            if value < 1 or value > 30:
                raise ValueError(f"Invalid day '{value}'. Please use a value between 1 and 30.")
        elif month == 2:
            if value < 1 or value > 29:
                raise ValueError(f"Invalid day '{value}'. Please use a value between 1 and 29.")
        return value

    @field_validator("hour")
    def validate_hour(cls, value):
        if value < 0 or value > 23:
            raise ValueError(f"Invalid hour '{value}'. Please use a value between 0 and 23.")
        return value

    @field_validator("minute")
    def validate_minute(cls, value):
        if value < 0 or value > 59:
            raise ValueError(f"Invalid minute '{value}'. Please use a value between 0 and 59.")
        return value

    @field_validator("year")
    def validate_year(cls, value):
        if value < 0 or value > 2100:
            raise ValueError(f"Invalid year '{value}'. Please use a value between 1800 and 2300.")
        return value


class TransitSubjectModel(BaseModel):
    """
    Represents the data needed to create a subject in the astrological data, specifically for transits.
    """

    year: int = Field(description="The year of birth.", examples=[1980])
    month: int = Field(description="The month of birth.", examples=[12])
    day: int = Field(description="The day of birth.", examples=[12])
    hour: int = Field(description="The hour of birth.", examples=[12])
    minute: int = Field(description="The minute of birth.", examples=[12])
    longitude: float = Field(description="The longitude of the birth location. Defaults on London.", examples=[0])
    latitude: float = Field(description="The latitude of the birth location. Defaults on London.", examples=[51.4825766])
    city: str = Field(description="The name of city of birth.", examples=["London"])
    timezone: str = Field(description="The timezone of the birth location.", examples=["Europe/London"])
    date: str = Field(description="The date of the transit.", examples=["2021-06-16"])
    time: str = Field(description="The time of the transit.", examples=["10:10"])
    zodiac_type: Optional[str] = Field(default="Tropic", description="The type of zodiac used (Tropic or Sidereal).", examples=["Tropic"])


class BirthChartRequestModel(BaseModel):
    """
    The request model for the Birth Chart endpoint.
    """

    subject: SubjectModel = Field(description="The name of the person to get the Birth Chart for.")
    new_settings: KerykeionChartSettingsModel | None | Literal[False] = Field(default=False, description="The settings model for the Kerykeion library.", examples=[False])


class SynastryChartRequestModel(BaseModel):
    """
    The request model for the Synastry Chart endpoint.
    """

    first_subject: SubjectModel = Field(description="The name of the person to get the Birth Chart for.")
    second_subject: SubjectModel = Field(description="The name of the person to get the Birth Chart for.")
    new_settings: KerykeionChartSettingsModel | None | Literal[False] = Field(default=False, description="The settings model for the Kerykeion library.", examples=[False])


class TransitChartRequestModel(BaseModel):
    """
    The request model for the Transit Chart endpoint.
    """

    first_subject: SubjectModel = Field(description="The name of the person to get the Birth Chart for.")
    transit_subject: TransitSubjectModel = Field(description="The name of the person to get the Birth Chart for.")
    new_settings: KerykeionChartSettingsModel | None | Literal[False] = Field(default=False, description="The settings model for the Kerykeion library.", examples=[False])


class BirthDataRequestModel(BaseModel):
    """
    The request model for the Birth Data endpoint.
    """

    subject: SubjectModel = Field(description="The name of the person to get the Birth Chart for.")


class RelationshipScoreRequestModel(BaseModel):
    """
    The request model for the Relationship Score endpoint.
    """

    first_subject: SubjectModel = Field(description="The name of the person to get the Birth Chart for.")
    second_subject: SubjectModel = Field(description="The name of the person to get the Birth Chart for.")


class SynastryAspectsRequestModel(BaseModel):
    """
    The request model for the Aspects endpoint.
    """

    first_subject: SubjectModel = Field(description="The name of the person to get the Birth Chart for.")
    second_subject: SubjectModel = Field(description="The name of the person to get the Birth Chart for.")
    new_settings: KerykeionChartSettingsModel | None | Literal[False] = Field(default=False, description="The settings model for the Kerykeion library.", examples=[False])


class NatalAspectsRequestModel(BaseModel):
    """
    The request model for the Birth Data endpoint.
    """

    subject: SubjectModel = Field(description="The name of the person to get the Birth Chart for.")
    new_settings: KerykeionChartSettingsModel | None | Literal[False] = Field(default=False, description="The settings model for the Kerykeion library.", examples=[False])
