class Solution(object):
    def missingRolls(self, rolls, mean, n):
        """
        :type rolls: List[int]
        :type mean: int
        :type n: int
        :rtype: List[int]
        """
        m = len(rolls)  # datos que si tenemos
        total_sum = mean * (n + m)  # La suma que deberían dar todos los dados juntos
        observed_sum = sum(rolls)  # suma de los dados que sí registramos
        missing_sum = total_sum - observed_sum  # Lo que deben sumar los dados faltantes

        # Condición de imposibilidad
        if (
            missing_sum < n or missing_sum > 6 * n
        ):  # si los n dados no pueden sumar eso (muy poquito o demasiado grande), no hay solución
            return []

        # Construir la respuesta
        base, extra = divmod(missing_sum, n)
        result = [base] * n
        for i in range(extra):
            result[i] += 1

        return result
