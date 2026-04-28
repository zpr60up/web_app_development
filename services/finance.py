from datetime import datetime, date
import calendar

class FinanceService:
    @staticmethod
    def calculate_custom_month_range(target_date: date, start_day: int):
        """
        根據給定的日期與自訂月起始日，計算「財務月」的起迄日期。
        """
        year = target_date.year
        month = target_date.month
        
        if target_date.day < start_day:
            month -= 1
            if month == 0:
                month = 12
                year -= 1
                
        start_date = date(year, month, start_day)
        
        next_month = month + 1
        next_year = year
        if next_month == 13:
            next_month = 1
            next_year += 1
            
        try:
            next_start_date = date(next_year, next_month, start_day)
        except ValueError:
            last_day = calendar.monthrange(next_year, next_month)[1]
            next_start_date = date(next_year, next_month, last_day)
            
        import datetime as dt
        end_date = next_start_date - dt.timedelta(days=1)
        
        return start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')
