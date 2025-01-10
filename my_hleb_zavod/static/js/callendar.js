let currentDate = new Date();

        function renderCalendar() {
            const monthDays = document.getElementById("days-grid");
            monthDays.innerHTML = ""; // Очистка предыдущих дней
            
            const year = currentDate.getFullYear();
            const month = currentDate.getMonth();
            
            // Обновление отображаемого месяца
            document.getElementById("month-display").innerText = currentDate.toLocaleString('default', { month: 'long', year: 'numeric' });

            // Получение первого и последнего дня месяца
            const firstDay = new Date(year, month, 1);
            const lastDay = new Date(year, month + 1, 0);
            
            // Заполнение дней месяца
            for (let i = 1; i <= lastDay.getDate(); i++) {
                const dayDate = new Date(year, month, i);
                const isWorkingDay = {{ work_days_dict|json_script:"work_days_dict" }}[dayDate.toISOString().split('T')[0]]; // Проверка на рабочий день
                
                const dayCell = document.createElement("div");
                dayCell.className = "four wide column";
                dayCell.innerHTML = `<div class='day ${isWorkingDay ? 'working' : 'non-working'}' onclick='selectDay("${dayDate.toISOString().split('T')[0]}", ${isWorkingDay})'>${i}</div>`;
                monthDays.appendChild(dayCell);
            }
        }

        function selectDay(date, isWorking) {
            document.getElementById("selected-date").value = date;
            document.getElementById("is-working-day").value = !isWorking; // Переключение значения
            document.getElementById("workdays-form").style.display = "block"; // Показать форму
        }

        function changeMonth(delta) {
            currentDate.setMonth(currentDate.getMonth() + delta);
            renderCalendar();
        }

        renderCalendar();