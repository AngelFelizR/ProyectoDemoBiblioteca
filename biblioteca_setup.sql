-- =============================================
-- Script de Base de Datos: BibliotecaDB
-- Sistema de Gestión de Biblioteca
-- =============================================

USE [BibliotecaDB]
GO

-- =============================================
-- TABLA: Autores
-- =============================================
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Autores]') AND type in (N'U'))
BEGIN
    CREATE TABLE [dbo].[Autores](
        [AutorID] [int] IDENTITY(1,1) NOT NULL,
        [Nombre] [nvarchar](100) NOT NULL,
        [Apellido] [nvarchar](100) NOT NULL,
        [Nacionalidad] [nvarchar](50) NULL,
        [FechaNacimiento] [date] NULL,
        [Biografia] [nvarchar](500) NULL,
        [FechaRegistro] [datetime] DEFAULT GETDATE(),
        CONSTRAINT [PK_Autores] PRIMARY KEY CLUSTERED ([AutorID] ASC)
    )
END
GO

-- =============================================
-- TABLA: Categorias
-- =============================================
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Categorias]') AND type in (N'U'))
BEGIN
    CREATE TABLE [dbo].[Categorias](
        [CategoriaID] [int] IDENTITY(1,1) NOT NULL,
        [NombreCategoria] [nvarchar](100) NOT NULL,
        [Descripcion] [nvarchar](300) NULL,
        CONSTRAINT [PK_Categorias] PRIMARY KEY CLUSTERED ([CategoriaID] ASC),
        CONSTRAINT [UK_NombreCategoria] UNIQUE ([NombreCategoria])
    )
END
GO

-- =============================================
-- TABLA: Libros
-- =============================================
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Libros]') AND type in (N'U'))
BEGIN
    CREATE TABLE [dbo].[Libros](
        [LibroID] [int] IDENTITY(1,1) NOT NULL,
        [Titulo] [nvarchar](200) NOT NULL,
        [ISBN] [nvarchar](20) NOT NULL,
        [AutorID] [int] NOT NULL,
        [CategoriaID] [int] NOT NULL,
        [FechaPublicacion] [date] NULL,
        [Editorial] [nvarchar](100) NULL,
        [NumeroPaginas] [int] NULL,
        [CopiasDisponibles] [int] DEFAULT 0,
        [CopiasTotal] [int] DEFAULT 0,
        [Descripcion] [nvarchar](500) NULL,
        [FechaRegistro] [datetime] DEFAULT GETDATE(),
        CONSTRAINT [PK_Libros] PRIMARY KEY CLUSTERED ([LibroID] ASC),
        CONSTRAINT [UK_ISBN] UNIQUE ([ISBN]),
        CONSTRAINT [FK_Libros_Autores] FOREIGN KEY ([AutorID]) REFERENCES [dbo].[Autores]([AutorID]),
        CONSTRAINT [FK_Libros_Categorias] FOREIGN KEY ([CategoriaID]) REFERENCES [dbo].[Categorias]([CategoriaID])
    )
END
GO

-- =============================================
-- TABLA: Usuarios
-- =============================================
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Usuarios]') AND type in (N'U'))
BEGIN
    CREATE TABLE [dbo].[Usuarios](
        [UsuarioID] [int] IDENTITY(1,1) NOT NULL,
        [NumeroCarnet] [nvarchar](20) NOT NULL,
        [Nombre] [nvarchar](100) NOT NULL,
        [Apellido] [nvarchar](100) NOT NULL,
        [Email] [nvarchar](100) NOT NULL,
        [Telefono] [nvarchar](20) NULL,
        [Direccion] [nvarchar](200) NULL,
        [FechaRegistro] [datetime] DEFAULT GETDATE(),
        [Estado] [nvarchar](20) DEFAULT 'Activo',
        CONSTRAINT [PK_Usuarios] PRIMARY KEY CLUSTERED ([UsuarioID] ASC),
        CONSTRAINT [UK_NumeroCarnet] UNIQUE ([NumeroCarnet]),
        CONSTRAINT [UK_Email] UNIQUE ([Email])
    )
END
GO

-- =============================================
-- TABLA: Prestamos
-- =============================================
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Prestamos]') AND type in (N'U'))
BEGIN
    CREATE TABLE [dbo].[Prestamos](
        [PrestamoID] [int] IDENTITY(1,1) NOT NULL,
        [LibroID] [int] NOT NULL,
        [UsuarioID] [int] NOT NULL,
        [FechaPrestamo] [datetime] DEFAULT GETDATE(),
        [FechaDevolucionEsperada] [date] NOT NULL,
        [FechaDevolucionReal] [datetime] NULL,
        [Estado] [nvarchar](20) DEFAULT 'Prestado',
        [Multa] [decimal](10,2) DEFAULT 0,
        CONSTRAINT [PK_Prestamos] PRIMARY KEY CLUSTERED ([PrestamoID] ASC),
        CONSTRAINT [FK_Prestamos_Libros] FOREIGN KEY ([LibroID]) REFERENCES [dbo].[Libros]([LibroID]),
        CONSTRAINT [FK_Prestamos_Usuarios] FOREIGN KEY ([UsuarioID]) REFERENCES [dbo].[Usuarios]([UsuarioID])
    )
END
GO

-- =============================================
-- DATOS DE PRUEBA
-- =============================================

-- Insertar Categorías
SET IDENTITY_INSERT [dbo].[Categorias] ON
INSERT INTO [dbo].[Categorias] (CategoriaID, NombreCategoria, Descripcion) VALUES
(1, 'Ficción', 'Novelas y cuentos de ficción'),
(2, 'Ciencia', 'Libros científicos y académicos'),
(3, 'Historia', 'Libros de historia y biografías'),
(4, 'Tecnología', 'Programación, informática y tecnología'),
(5, 'Literatura Clásica', 'Clásicos de la literatura universal')
SET IDENTITY_INSERT [dbo].[Categorias] OFF
GO

-- Insertar Autores
SET IDENTITY_INSERT [dbo].[Autores] ON
INSERT INTO [dbo].[Autores] (AutorID, Nombre, Apellido, Nacionalidad, FechaNacimiento, Biografia) VALUES
(1, 'Gabriel', 'García Márquez', 'Colombiana', '1927-03-06', 'Escritor y periodista colombiano, Premio Nobel de Literatura 1982'),
(2, 'Miguel', 'de Cervantes', 'Española', '1547-09-29', 'Novelista, poeta y dramaturgo español'),
(3, 'Stephen', 'Hawking', 'Británica', '1942-01-08', 'Físico teórico, cosmólogo y divulgador científico'),
(4, 'Robert', 'Martin', 'Estadounidense', '1952-12-05', 'Ingeniero de software y autor de libros de programación'),
(5, 'Isaac', 'Asimov', 'Estadounidense', '1920-01-02', 'Escritor y profesor de bioquímica, conocido por obras de ciencia ficción')
SET IDENTITY_INSERT [dbo].[Autores] OFF
GO

-- Insertar Libros
SET IDENTITY_INSERT [dbo].[Libros] ON
INSERT INTO [dbo].[Libros] (LibroID, Titulo, ISBN, AutorID, CategoriaID, FechaPublicacion, Editorial, NumeroPaginas, CopiasDisponibles, CopiasTotal, Descripcion) VALUES
(1, 'Cien Años de Soledad', '978-0307474728', 1, 1, '1967-05-30', 'Editorial Sudamericana', 417, 3, 5, 'La historia de la familia Buendía a lo largo de siete generaciones'),
(2, 'Don Quijote de la Mancha', '978-8420412146', 2, 5, '1605-01-16', 'Francisco de Robles', 863, 2, 4, 'Las aventuras de un hidalgo que pierde la cordura por leer libros de caballería'),
(3, 'Breve Historia del Tiempo', '978-0553380163', 3, 2, '1988-04-01', 'Bantam Books', 212, 4, 4, 'Del big bang a los agujeros negros'),
(4, 'Clean Code', '978-0132350884', 4, 4, '2008-08-01', 'Prentice Hall', 464, 5, 6, 'Manual de estilo para el desarrollo ágil de software'),
(5, 'Fundación', '978-0553293357', 5, 1, '1951-06-01', 'Gnome Press', 255, 2, 3, 'Primera novela de la saga de la Fundación')
SET IDENTITY_INSERT [dbo].[Libros] OFF
GO

-- Insertar Usuarios
SET IDENTITY_INSERT [dbo].[Usuarios] ON
INSERT INTO [dbo].[Usuarios] (UsuarioID, NumeroCarnet, Nombre, Apellido, Email, Telefono, Direccion, Estado) VALUES
(1, 'USR001', 'Juan', 'Pérez', 'juan.perez@email.com', '809-555-0101', 'Calle Principal #123', 'Activo'),
(2, 'USR002', 'María', 'González', 'maria.gonzalez@email.com', '809-555-0102', 'Av. Independencia #456', 'Activo'),
(3, 'USR003', 'Carlos', 'Rodríguez', 'carlos.rodriguez@email.com', '809-555-0103', 'Calle Secundaria #789', 'Activo'),
(4, 'USR004', 'Ana', 'Martínez', 'ana.martinez@email.com', '809-555-0104', 'Av. 27 de Febrero #321', 'Activo')
SET IDENTITY_INSERT [dbo].[Usuarios] OFF
GO

-- Insertar Préstamos de Ejemplo
SET IDENTITY_INSERT [dbo].[Prestamos] ON
INSERT INTO [dbo].[Prestamos] (PrestamoID, LibroID, UsuarioID, FechaPrestamo, FechaDevolucionEsperada, FechaDevolucionReal, Estado, Multa) VALUES
(1, 1, 1, '2025-11-01', '2025-11-15', '2025-11-14', 'Devuelto', 0),
(2, 3, 2, '2025-11-10', '2025-11-24', NULL, 'Prestado', 0),
(3, 4, 3, '2025-11-12', '2025-11-26', NULL, 'Prestado', 0)
SET IDENTITY_INSERT [dbo].[Prestamos] OFF
GO

-- =============================================
-- ÍNDICES PARA OPTIMIZACIÓN
-- =============================================
CREATE NONCLUSTERED INDEX [IX_Libros_AutorID] ON [dbo].[Libros] ([AutorID])
GO

CREATE NONCLUSTERED INDEX [IX_Libros_CategoriaID] ON [dbo].[Libros] ([CategoriaID])
GO

CREATE NONCLUSTERED INDEX [IX_Prestamos_Estado] ON [dbo].[Prestamos] ([Estado])
GO

CREATE NONCLUSTERED INDEX [IX_Usuarios_Estado] ON [dbo].[Usuarios] ([Estado])
GO

PRINT 'Base de datos BibliotecaDB creada exitosamente con datos de prueba'
GO
