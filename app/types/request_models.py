from pydantic import BaseModel, Field, field_validator
from typing import Optional, get_args, Union
from pytz import all_timezones
from kerykeion.kr_types.kr_literals import KerykeionChartTheme, KerykeionChartLanguage, SiderealMode, ZodiacType
from abc import ABC

class AbstractBaseSubjectModel(BaseModel, ABC):
    year: int = Field(description="The year of birth.", examples=[1980])
    month: int = Field(description="The month of birth.", examples=[12])
    day: int = Field(description="The day of birth.", examples=[12])
    hour: int = Field(description="The hour of birth.", examples=[12])
    minute: int = Field(description="The minute of birth.", examples=[12])
    longitude: float = Field(description="The longitude of the birth location. Defaults on London.", examples=[0])
    latitude: float = Field(description="The latitude of the birth location. Defaults on London.", examples=[51.4825766])
    city: str = Field(description="The name of city of birth.", examples=["London"])
    nation: Optional[str] = Field(default="null", description="The name of the nation of birth.", examples=["GB"], min_length=2, max_length=2)
    timezone: str = Field(description="The timezone of the birth location.", examples=["Europe/London"])


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
            raise ValueError(f"Invalid timezone '{value}'. Please use a valid timezone. You can find a list of valid timezones at https://en.wikipedia.org/wiki/List_of_tz_database_time_zones.")
        return value

    @field_validator("month")
    def validate_month(cls, value):
        if value < 1 or value > 12:
            raise ValueError(f"Invalid month '{value}'. Please use a value between 1 and 12.")
        return value

    @field_validator("day")
    def validate_day(cls, value, values):
        month = values.data.get("month")

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

    @field_validator("nation")
    def validate_nation(cls, value):
        if not value:
            return "null"

class SubjectModel(AbstractBaseSubjectModel):
    name: str = Field(description="The name of the person to get the Birth Chart for.", examples=["John Doe"])
    zodiac_type: Optional[ZodiacType] = Field(default="Tropic", description="The type of zodiac used (Tropic or Sidereal).", examples=list(get_args(ZodiacType)))
    sidereal_mode: Union[SiderealMode, None] = Field(default=None, description="The sidereal mode used.", examples=[None])

    @field_validator("zodiac_type")
    def validate_zodiac_type(cls, value, info):
        if info.data.get('sidereal_mode') and value != "Sidereal":
            raise ValueError(f"Invalid zodiac_type '{value}'. Please use 'Sidereal' when sidereal_mode is set.")
        return value

    @field_validator("sidereal_mode")
    def validate_sidereal_mode(cls, value, info):
        # If sidereal mode is set, zodiac type must be Sidereal
        if value and info.data.get('zodiac_type') != "Sidereal":
            raise ValueError(f"Invalid sidereal_mode '{value}'. Please use 'Sidereal' as zodiac_type when sidereal_mode is set. If you want to use the default sidereal mode, do not set this field or set it to None.")
        return value

class TransitSubjectModel(AbstractBaseSubjectModel):
    ...

class BirthChartRequestModel(BaseModel):
    """
    The request model for the Birth Chart endpoint.
    """

    subject: SubjectModel = Field(description="The name of the person to get the Birth Chart for.")
    theme: Optional[KerykeionChartTheme] = Field(default="classic", description="The theme of the chart.", examples=["classic", "light", "dark", "dark-high-contrast"])
    language: Optional[KerykeionChartLanguage] = Field(default="EN", description="The language of the chart.", examples=list(get_args(KerykeionChartLanguage)))

class SynastryChartRequestModel(BaseModel):
    """
    The request model for the Synastry Chart endpoint.
    """

    first_subject: SubjectModel = Field(description="The name of the person to get the Birth Chart for.")
    second_subject: SubjectModel = Field(description="The name of the person to get the Birth Chart for.")
    theme: Optional[KerykeionChartTheme] = Field(default="classic", description="The theme of the chart.", examples=["classic", "light", "dark", "dark-high-contrast"])
    language: Optional[KerykeionChartLanguage] = Field(default="EN", description="The language of the chart.", examples=list(get_args(KerykeionChartLanguage)))

class TransitChartRequestModel(BaseModel):
    """
    The request model for the Transit Chart endpoint.
    """

    first_subject: SubjectModel = Field(description="The name of the person to get the Birth Chart for.")
    transit_subject: TransitSubjectModel = Field(description="The name of the person to get the Birth Chart for.")
    theme: Optional[KerykeionChartTheme] = Field(default="classic", description="The theme of the chart.", examples=["classic", "light", "dark", "dark-high-contrast"])
    language: Optional[KerykeionChartLanguage] = Field(default="EN", description="The language of the chart.", examples=list(get_args(KerykeionChartLanguage)))


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


class NatalAspectsRequestModel(BaseModel):
    """
    The request model for the Birth Data endpoint.
    """

    subject: SubjectModel = Field(description="The name of the person to get the Birth Chart for.")
