DROP TABLE IF EXISTS [dbo].[projects];
GO

CREATE TABLE [dbo].[projects] (
    [Id] [INT] IDENTITY(1,1) PRIMARY KEY,
    [Name] [NVARCHAR](50) NOT NULL,
    [Created_Date] [DATE] NOT NULL,
    [MD5_Hash] AS CAST(
        HASHBYTES(
            'MD5',
            CONCAT(
                Name,
                CONVERT(VARCHAR(10), Created_Date, 120)
            )
        )
    )
)
GO