-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/ixxC0b
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "MaritalStatus" (
    "Year" int   NOT NULL,
    "CountyName" varchar(200)   NOT NULL,
    "StateName" varchar(100)   NOT NULL,
    "NowMarriedPct" float   NOT NULL,
    "NowMarriedError" float   NOT NULL,
    "DivorcedPct" float   NOT NULL,
    "DivorcedError" float   NOT NULL,
    "SeparatedPct" float   NOT NULL,
    "SeparatedError" float   NOT NULL,
    "NeverMarriedPct" float   NOT NULL,
    "NeverMarriedError" float   NOT NULL,
    CONSTRAINT "pk_MaritalStatus" PRIMARY KEY (
        "Year","CountyName","StateName"
     )
);

CREATE TABLE "DebtToIncomeRatiosByYear" (
    "Year" int   NOT NULL,
    "CountyName" varchar(200)   NOT NULL,
    "StateName" varchar(100)   NOT NULL,
    "DtoI_low" float   NOT NULL,
    "DtoI_high" float   NOT NULL,
    CONSTRAINT "pk_DebtToIncomeRatiosByYear" PRIMARY KEY (
        "Year","CountyName","StateName"
     )
);

CREATE TABLE "DebtToIncomeRatiosByQtr" (
    "Year" int   NOT NULL,
    "Quarter" int   NOT NULL,
    "CountyName" varchar(200)   NOT NULL,
    "StateName" varchar(100)   NOT NULL,
    "DtoI_low" float   NOT NULL,
    "DtoI_high" float   NOT NULL,
    CONSTRAINT "pk_DebtToIncomeRatiosByQtr" PRIMARY KEY (
        "Year","Quarter","CountyName","StateName"
     )
);

CREATE TABLE "MortgageCosts_time_permitting" (
    "Year" int   NOT NULL,
    "CountyName" varchar(200)   NOT NULL,
    "StateName" varchar(100)   NOT NULL,
    "MonthlyMortgageBin" varchar(30)   NOT NULL,
    "NumHouseholds" bigint   NOT NULL,
    CONSTRAINT "pk_MortgageCosts_time_permitting" PRIMARY KEY (
        "Year","CountyName","StateName","MonthlyMortgageBin"
     )
);

CREATE TABLE "Income_time_permitting" (
    "Year" int   NOT NULL,
    "CountyName" varchar(200)   NOT NULL,
    "StateName" varchar(100)   NOT NULL,
    "IncomeBin" varchar(30)   NOT NULL,
    "NumHouseholds" bigint   NOT NULL,
    CONSTRAINT "pk_Income_time_permitting" PRIMARY KEY (
        "Year","CountyName","StateName","IncomeBin"
     )
);

-- REMOVING the FK relationship as the data is denormalized and there is no guarantee
-- that data exists for every county equally in both fact tables. The two tables should
-- be inner joined during analysis to properly evaluate marriage stats compared to debt
-- stats in counties where both stats exist
--ALTER TABLE "MaritalStatus" ADD CONSTRAINT "fk_MaritalStatus_Year_CountyName_StateName" --FOREIGN KEY("Year", "CountyName", "StateName")
--REFERENCES "DebtToIncomeRatiosByYear" ("Year", "CountyName", "StateName");

