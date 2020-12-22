#define P1364_VECVAL
#include "dpi_div.h"
#include "vpi_user.h"


void divider10(
    svBitVecVal* quotient,
    const svBitVecVal* divident,
    const svBitVecVal* divider)
{

   /* int n;
    char prev = 0;
    for (n = 0; n < SV_PACKED_DATA_NELEMS(10); n++)
    {
        quotient[n] = divider[n] | quotient[n] | prev;
        if((divider[n] ^ quotient[n]) & divider[n])
            prev = 1;
        else
            prev = 0;
    }*/
    
    
    
    *quotient = *divident / *divider;
    
}



