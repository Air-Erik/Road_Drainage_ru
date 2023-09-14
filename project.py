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
        o.error_text = 'Please input the data'
    else:
        try:
            num = float(o.value.replace(',', '.'))
        except ValueError:
            o.error_text = 'Please enter a float number'
            o.value = ''
            return None
        if num < min or num > max:
            o.error_text = f'Must be in the range from {min} to {max}'
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
        fin.value = f'The total thickness of the subbase layer is {h_fin:.2f} m considering the allowance for capillary moisture rise {soil} m'
        page.update()


    # Input data for calculation
    txt_Kf = ft.TextField(label='Input the subbase filtration coefficient', width=250)
    txt_L = ft.TextField(label='Input the the length of the filtration path', width=250)
    txt_B = ft.TextField(label='Input the width of the roadway', width=250)

    txt_i = ft.Dropdown(
        label='Slope',
        hint_text='Choose the slope of the subbase layer',
        options=[
            ft.dropdown.Option(text='20‰', key=0.02),
            ft.dropdown.Option(text='30‰', key=0.03),
            ft.dropdown.Option(text='40‰', key=0.04),
        ], width=250,
    )
    txt_soil = ft.Dropdown(
        label='Soil',
        hint_text='Choose the subbase soil type',
        options=[
            ft.dropdown.Option(text='Fine sand', key=0.20),
            ft.dropdown.Option(text='Medium sand', key=0.15),
            ft.dropdown.Option(text='Coarse sand', key=0.10),
        ], width=250,
    )
    txt_profile = ft.Dropdown(
        label='Cross-sectional profile',
        hint_text='Choose the type of cross-sectional profile',
        options=[
            ft.dropdown.Option(text='Single-slope cross-sectional profile', key=1),
            ft.dropdown.Option(text='Dual-slope cross-sectional profile', key=0.5),
        ], width=250,
    )

    txt_q = ft.TextField(
        label='Input volume of the average water inflow (table 13)', width=250
    )
    txt_Kpik = ft.TextField(label='Input volume of the peak coefficient (table 14)', width=250)
    txt_Kg = ft.TextField(label='Input volume of the hydrological reserve coefficient (table 14)', width=250)
    txt_Kr = ft.TextField(label='Input volume of the reduction water inflow coefficient (table 15)', width=250)
    txt_Kv = ft.TextField(label='Input volume of the bulking coefficient', width=250)
    fin = ft.Text('', size=40, color=ft.colors.GREEN_700)

    #Tables
    excel_13 = ExcelToFlet('Table_13.xlsx', width=900)

    excel_14 = ExcelToFlet('Table_14.xlsx', width=900)

    excel_15 = ExcelToFlet('Table_15.xlsx', width=900)

    item_13 = ft.Column(controls=[
        ft.Text('Table 13\nThe volume of water entering the roadbed from the soil', width=900),
        excel_13
    ])

    item_14 = ft.Column(controls=[
        ft.Text('Table 14\nThe peak coefficient that takes into account the non-steady state of water inflow due to uneven thawing\n and atmospheric precipitation', width=900),
        excel_14,
        ft.Text('''Note:\n
                1. For non-dusty soils, Kg = 1.0\n
                2. The numerator contains the values of Kg for roads of categories I and II, and
                the denominator - for categories III and IV\n''', width=700)
    ])

    item_15 = ft.Column(controls=[
        ft.Text('Table 15\nCoefficient accounting for water inflow reduction for the working layer soil', width=900),
        excel_15,
        ft.Text('''Note:\n
                1. When using dusty soils, the coefficient Kr = 1.0\n
                2. If multiple measures are provided, each of them is considered separately\n''', width=900)
    ])

    #Adding interface elements to the page
    page.add(ft.Text('Initial data for calculation', size=50))

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
            ft.ElevatedButton("Calculate", on_click=button_clicked)
        ], wrap=True)
    )

    page.add(
        fin
    )


ft.app(target=main, view=ft.AppView.WEB_BROWSER)
