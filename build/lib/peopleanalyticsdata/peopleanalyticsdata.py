import pkg_resources
import pandas as pd

#####################################################################
# Below is a list of all the functions which return datasets by name
#####################################################################

# charity_donation
def charity_donation():
    """Return a dataframe about the charity donation.

    Contains the following fields:
         #   Column           Non-Null Count  Dtype 
        ---  ------           --------------  ----- 
         0   n_donations      354 non-null    int64 
         1   total_donations  354 non-null    int64 
         2   time_donating    354 non-null    int64 
         3   recent_donation  354 non-null    int64 
         4   last_donation    354 non-null    int64 
         5   gender           354 non-null    object
         6   reside           354 non-null    object
         7   age              354 non-null    int64 

    """
    stream = pkg_resources.resource_stream(__name__, 'data/charity_donation.csv')
    return pd.read_csv(stream)

# employee_survey
def employee_survey():
    """Return a dataframe about the employee survey.

    Contains the following fields:
         #   Column     Non-Null Count  Dtype
        ---  ------     --------------  -----
         0   Happiness  2833 non-null   int64
         1   Ben1       2833 non-null   int64
         2   Ben2       2833 non-null   int64
         3   Ben3       2833 non-null   int64
         4   Work1      2833 non-null   int64
         5   Work2      2833 non-null   int64
         6   Work3      2833 non-null   int64
         7   Man1       2833 non-null   int64
         8   Man2       2833 non-null   int64
         9   Man3       2833 non-null   int64
         10  Car1       2833 non-null   int64
         11  Car2       2833 non-null   int64
         12  Car3       2833 non-null   int64
         13  Car4       2833 non-null   int64

    """
    stream = pkg_resources.resource_stream(__name__, 'data/employee_survey.csv')
    return pd.read_csv(stream)

# health_insurance
def health_insurance():
    """Return a dataframe about the health insurance
    
    Contains the following fields:
    
         #   Column          Non-Null Count  Dtype 
        ---  ------          --------------  ----- 
         0   product         1453 non-null   object
         1   age             1453 non-null   int64 
         2   household       1453 non-null   int64 
         3   position_level  1453 non-null   int64 
         4   gender          1453 non-null   object
         5   absent          1453 non-null   int64 
    """
    stream = pkg_resources.resource_stream(__name__, 'data/health_insurance.csv')
    return pd.read_csv(stream)

# job_retention
def job_retention():
    """Return a dataframe about job retention
    
    Contains the following fields:
    
         #   Column     Non-Null Count  Dtype 
        ---  ------     --------------  ----- 
         0   gender     3770 non-null   object
         1   field      3770 non-null   object
         2   level      3770 non-null   object
         3   sentiment  3770 non-null   int64 
         4   intention  3770 non-null   int64 
         5   left       3770 non-null   int64 
         6   month      3770 non-null   int64 
    """
    stream = pkg_resources.resource_stream(__name__, 'data/job_retention.csv')
    return pd.read_csv(stream)

# managers
def managers():
    """Return a dataframe about managers
    
    Contains the following fields:
    
        #   Column             Non-Null Count  Dtype  
        ---  ------             --------------  -----  
         0   employee_id        571 non-null    object 
         1   performance_group  571 non-null    object 
         2   yrs_employed       571 non-null    float64
         3   manager_hire       571 non-null    object 
         4   test_score         571 non-null    int64  
         5   group_size         571 non-null    int64  
         6   concern_flag       571 non-null    object 
         7   mobile_flag        571 non-null    object 
         8   customers          571 non-null    int64  
         9   high_hours_flag    571 non-null    object 
         10  transfers          571 non-null    int64  
         11  reduced_schedule   571 non-null    object 
         12  city               571 non-null    object  
    """
    stream = pkg_resources.resource_stream(__name__, 'data/managers.csv')
    return pd.read_csv(stream)

# politics_survey
def politics_survey():
    """Return a dataframe about politics survey
    
    Contains the following fields:
    
        #   Column             Non-Null Count  Dtype  
        ---  ------   --------------  -----
         0   Overall  2108 non-null   int64
         1   Pol1     2108 non-null   int64
         2   Pol2     2108 non-null   int64
         3   Pol3     2108 non-null   int64
         4   Hab1     2108 non-null   int64
         5   Hab2     2108 non-null   int64
         6   Hab3     2108 non-null   int64
         7   Loc1     2108 non-null   int64
         8   Loc2     2108 non-null   int64
         9   Loc3     2108 non-null   int64
         10  Loc4     2108 non-null   int64
         11  Env1     2108 non-null   int64
         12  Env2     2108 non-null   int64
         13  Int1     2108 non-null   int64
         14  Int2     2108 non-null   int64
         15  Pers1    2108 non-null   int64
         16  Pers2    2108 non-null   int64
         17  Pers3    2108 non-null   int64
         18  Nat1     2108 non-null   int64
         19  Nat2     2108 non-null   int64
         20  Nat3     2108 non-null   int64
         21  Eco1     2108 non-null   int64
         22  Eco2     2108 non-null   int64  
    """
    stream = pkg_resources.resource_stream(__name__, 'data/politics_survey.csv')
    return pd.read_csv(stream)

def salespeople():
    """Return a dataframe about salespeople
    
    Contains the following fields:
    
         #   Column         Non-Null Count  Dtype  
        ---  ------         --------------  -----  
         0   promoted       351 non-null    int64  
         1   sales          350 non-null    float64
         2   customer_rate  350 non-null    float64
         3   performance    350 non-null    float64  
    """
    stream = pkg_resources.resource_stream(__name__, 'data/salespeople.csv')
    return pd.read_csv(stream)

# soccer
def soccer():
    """Return a dataframe about soccer
    
    Contains the following fields:
    
        #   Column       Non-Null Count  Dtype 
        ---  ------       --------------  ----- 
         0   discipline   2291 non-null   object
         1   n_yellow_25  2291 non-null   int64 
         2   n_red_25     2291 non-null   int64 
         3   position     2291 non-null   object
         4   result       2291 non-null   object
         5   country      2291 non-null   object
         6   level        2291 non-null   int64
    """
    stream = pkg_resources.resource_stream(__name__, 'data/soccer.csv')
    return pd.read_csv(stream)

# sociological data
def sociological_data():
    """Return a dataframe about sociological data
    
    Contains the following fields:
    
        #   Column       Non-Null Count  Dtype 
        ---  ------       --------------  ----- 
         0   discipline   2291 non-null   object
         1   n_yellow_25  2291 non-null   int64 
         2   n_red_25     2291 non-null   int64 
         3   position     2291 non-null   object
         4   result       2291 non-null   object
         5   country      2291 non-null   object
         6   level        2291 non-null   int64
    """
    stream = pkg_resources.resource_stream(__name__, 'data/sociological_data.csv')
    return pd.read_csv(stream)

# speed_dating
def speed_dating():
    """Return a dataframe about speed dating
    
    Contains the following fields:
    
         #   Column    Non-Null Count  Dtype  
        ---  ------    --------------  -----  
         0   iid       8378 non-null   int64  
         1   gender    8378 non-null   int64  
         2   match     8378 non-null   int64  
         3   samerace  8378 non-null   int64  
         4   race      8315 non-null   float64
         5   goal      8299 non-null   float64
         6   dec       8378 non-null   int64  
         7   attr      8176 non-null   float64
         8   intel     8082 non-null   float64
         9   prob      8069 non-null   float64
         10  agediff   8180 non-null   float64
    """
    stream = pkg_resources.resource_stream(__name__, 'data/speed_dating.csv')
    return pd.read_csv(stream)

# ugtests
def ugtests():
    """Return a dataframe about ugtests
    
    Contains the following fields:
    
          #   Column  Non-Null Count  Dtype
        ---  ------  --------------  -----
         0   Yr1     975 non-null    int64
         1   Yr2     975 non-null    int64
         2   Yr3     975 non-null    int64
         3   Final   975 non-null    int64
    """
    stream = pkg_resources.resource_stream(__name__, 'data/ugtests.csv')
    return pd.read_csv(stream)


