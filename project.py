import flet as ft
from simpledt import ExcelDataTable


def ExcelToFlet(name, width=900):
    df = ExcelDataTable(name)
    excel = ft.Row([df.datatable], width=width)
    return excel


def y_coef(x: float, i: int) -> float:
    if i == 0.02:
        y = 20.284 * x - 0.0471684
    elif i == 0.03:
        y = 19.348 * x - 0.0582248
    else:
        y = 18.354 * x - 0.0691404
    return y


def check(o, min, max):
    if not o.value:
        o.error_text = 'Введите значение'
    else:
        try:
            num = float(o.value.replace(',', '.'))
        except ValueError:
            o.error_text = 'Ввидите число'
            o.value = ''
            return None
        if num < min or num > max:
            o.error_text = f'Значение должно быть в диапазоне от {min} до {max}'
        else:
            o.error_text = ''
            return num


def main(page: ft.Page):
    page.scroll = 'auto'


    def button_clicked(e):
        Kf = check(txt_Kf, 1, 10)
        l = check(txt_L, 1, 30)
        b = check(txt_B, 1, 30)
        q = check(txt_q, 1.5, 5)
        Kpik = check(txt_Kpik, 1.3, 1.7)
        Kg = check(txt_Kg, 1.0, 1.3)
        Kr = check(txt_Kr, 0.7, 1.0)
        Kv = check(txt_Kv, 0.1, 2)
        page.update()
        i = float(txt_i.value)
        soil = float(txt_soil.value)
        profile = float(txt_profile.value)

        # Calculation
        qr = q * Kpik * Kg * Kr * Kv / 1000
        q1 = qr * b * profile
        x_coef = q1 / Kf
        h_dop = y_coef(x_coef, i) * l / 3.5
        h_fin = h_dop + soil
        fin.value = f'Полная толщина подстилающего слоя равна {h_fin:.2f} м с учетом дополнительного защитного слоя {soil} м'
        page.update()


    # Input data for calculation
    txt_Kf = ft.TextField(label='Введите коэффициент фильтрации для подстилающего слоя', width=250)
    txt_L = ft.TextField(label='Введите длину пути фильтрации', width=250)
    txt_B = ft.TextField(label='Введите ширину покрытия автомобильной дороги', width=250)

    txt_i = ft.Dropdown(
        label='Уклон',
        hint_text='Выберите уклон подстилающего слоя',
        options=[
            ft.dropdown.Option(text='20‰', key=0.02),
            ft.dropdown.Option(text='30‰', key=0.03),
            ft.dropdown.Option(text='40‰', key=0.04),
        ], width=250,
    )
    txt_soil = ft.Dropdown(
        label='Материал',
        hint_text='Выберите материал подстилающего слоя',
        options=[
            ft.dropdown.Option(text='Мелкий песок', key=0.20),
            ft.dropdown.Option(text='Средний песок', key=0.15),
            ft.dropdown.Option(text='Крупный песок', key=0.10),
        ], width=250,
    )
    txt_profile = ft.Dropdown(
        label='Поперечный профиль',
        hint_text='Выберите тип поперечного профиля',
        options=[
            ft.dropdown.Option(text='Односкатный', key=1),
            ft.dropdown.Option(text='Двускатный', key=0.5),
        ], width=250,
    )

    txt_q = ft.TextField(
        label='Введите значение притока воды в подстилающий слой (по таблице 13)', width=250
    )
    txt_Kpik = ft.TextField(label='Введите значение коэффициента "пик" (по таблице 14)', width=250)
    txt_Kg = ft.TextField(label='Введите значение коэффициента гидрологического запаса (по таблице 14)', width=250)
    txt_Kr = ft.TextField(label='Введите значение коэффициента снижение притока воды (по таблице 15)', width=250)
    txt_Kv = ft.TextField(label='Введите значение коэффициента вогнутости', width=250)
    fin = ft.Text('', size=40, color=ft.colors.GREEN_700)

    #Tables
    excel_13 = ExcelToFlet('Table_13.xlsx', width=900)

    excel_14 = ExcelToFlet('Table_14.xlsx', width=900)

    excel_15 = ExcelToFlet('Table_15.xlsx', width=900)

    item_13 = ft.Column(controls=[
        ft.Text('Таблица 13\nОбъем воды, поступающей в основание дорожной одежды из грунта', width=900),
        excel_13
    ])

    item_14 = ft.Column(controls=[
        ft.Text('Таблица 14\nЗначения коэффициента "пик" Kпик и коэффициента гидрологического запаса Kг', width=900),
        excel_14,
        ft.Text('''Примечания:\n
                1. Для непылеватых грунтов, Kг = 1.0\n
                2. В числителе указаны значения Kг для дорог категорий I и II
                в знаменателе - для категорий III и IV\n''', width=700)
    ])

    item_15 = ft.Column(controls=[
        ft.Text('Таблица 15\nЗначения коэффициента Кр, учитывающего снижение притока воды в дренирующий слой', width=900),
        excel_15,
        ft.Text('''Примечания:\n
                1. При применении пылеватых грунтов коэффициент Kр = 1.0\n
                2. Если предусмотрено несколько мероприятий, то каждое из них учитывают в отдельности\n''', width=900)
    ])

    #Adding interface elements to the page
    page.add(ft.Text('Исходные данные для расчета', size=50))

    page.add(
        ft.Row(controls=[
            txt_Kf,
            txt_L,
            txt_B,
            txt_i,
            txt_soil,
            txt_profile
        ], wrap=True)
    )

    page.add(
        ft.Row(controls=[
            item_13,
            item_14,
            item_15
        ], vertical_alignment=ft.CrossAxisAlignment.START, scroll=ft.ScrollMode.AUTO)
    )

    page.add(
        ft.Row(controls=[
            txt_q,
            txt_Kpik,
            txt_Kg,
            txt_Kr,
            txt_Kv,
            ft.ElevatedButton("Расчитать", on_click=button_clicked)
        ], wrap=True)
    )

    page.add(
        fin
    )


ft.app(target=main, view=ft.AppView.WEB_BROWSER)
