#define P1364_VECVAL
#include "dpi_max.h"
#include "vpi_user.h"




/*svBitVecVal max(const svBitVecVal x, const svBitVecVal y)
{
    return (x > y) ? x : y;
}  */

void max_arr(const svOpenArrayHandle p, int n, svBitVecVal *res  )
{   if (n<=0) return;
    int dim = 1;
    svBitVecVal *s = (svBitVecVal*) svGetArrayPtr(p);
    *res = *s  ;
    if (n<=0) return;
    max_arr(p, n - 1, res );
    if ( *(svBitVecVal*)svGetArrElemPtr1(p, n-1) >= *res)
    {
        *res = *(svBitVecVal*)svGetArrElemPtr1(p, n-1);
    }
    //*res = max(*(svBitVecVal*)svGetArrElemPtr1(p, n-1), *res);
}


